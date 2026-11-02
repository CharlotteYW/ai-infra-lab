# P1.W1: Transformer and LLM Inference Fundamentals

## Overview

First module of [Phase 1](README.md). Target: 10 hours, with up to 2 additional hours for
remediation/exploration. Tensor familiarity is self-reported; verify relevant reasoning
before accelerating. Setup and agent-provided tests are not evidence of learning.

Use Python 3.11/PyTorch on CPU float32. MPS is optional for environment exploration, not
an exercise requirement. No model weights, model API, cloud account, or NVIDIA GPU is needed.

| Activity | Hours |
| --- | --- |
| Environment verification and short diagnostic | 1 |
| Selected reading and guided examples | 2.5 |
| Implement and test attention | 3 |
| Implement a bounded greedy generation loop | 1 |
| Trace inference computation and memory | 1 |
| Review, assessment, and progress recording | 1.5 |

## Learning objectives

- **Conceptual:** trace tokens -> embeddings -> Transformer blocks -> logits -> next token.
  Explain Q/K/V, scaling, softmax, causal masking, heads, residual connections, and positional
  information. Distinguish parameters, activations, and cached state; explain prefill/decode
  and evaluation versus gradient-recording behavior.
- **Implementation:** write attention from primitive tensor operations and a bounded greedy
  token loop, with clear inputs/outputs and no dependency on a pretrained model.
- **Performance analysis:** trace naive full-prefix recomputation and identify candidate
  reusable state; calculate tensor element/byte counts under explicit dtype assumptions.
- **System design:** explain why a deterministic callback is useful for testing generation
  control flow and which real inference behaviors it does not model.

## Start with a short diagnostic

Mentor: ask one question at a time, wait for the response, and use progressive hints.
The first question is:

> Given Q, K, and V shaped [2, 4, 8, 16], what are the intermediate attention shapes?

Follow with a brief autograd/evaluation question and a prompt-versus-next-token question
if needed. Limit the opening diagnostic to about 15 minutes. Record actual responses and
assistance; do not grade the learner from a self-report or start with an answer dump.

## Study materials

Selected links/sections were checked on 2026-11-01. These times are included above.

| Resource | Task and classification | Hours | Expected takeaway |
| --- | --- | --- | --- |
| [D2L Transformer chapter](https://d2l.ai/chapter_attention-mechanisms-and-transformers/transformer.html), with linked Q/K/V, attention scoring, multi-head, and positional-encoding sections | Required; inspect diagrams and trace shapes; avoid copying a complete implementation | 1.5 | Explain model data flow and distinguish decoder-only inference from encoder-decoder examples |
| [PyTorch Autograd](https://docs.pytorch.org/tutorials/beginner/introyt/autogradyt_tutorial.html) | Required; selected reading and a tiny graph experiment | 0.5 | Explain gradient tracking and its relationship to inference |
| [PyTorch SDPA tutorial](https://docs.pytorch.org/tutorials/intermediate/scaled_dot_product_attention_tutorial.html) | Required; inspect interface/causal behavior after the first attempt | 0.5 | Use a framework oracle to verify behavior without replacing the learner implementation |

Optional resources from the phase overview can wait. Reading is a means to the objectives,
not a requirement to finish entire books or tutorials.

## Key concepts and guided work

The core expression is `softmax(Q K^T / sqrt(d_k)) V`, with shapes, softmax dimension, and
causal visibility to be justified by the learner. Token IDs are discrete vocabulary indices;
logits score the next-token candidates. Attention is one component of a Transformer block,
not the entire model. Discuss how embeddings, projections, residuals, normalization, the
MLP, and positional information fit around it, without implementing the full decoder yet.

Use a small hand-worked example before coding. The mentor should ask the learner to
predict its shapes and visibility, then check reasoning. Avoid giving the full algorithm
as a worked solution. Discuss tokenization versus characters and demonstrate the distinction
with a small explanatory example; a tokenizer implementation is outside this week's scope.

## Exercise A: Attention (3 hours)

**Problem/objective:** implement scaled dot-product self-attention and demonstrate that
causal output does not depend on future tokens.

**Starting point:** the [learner stub](../../labs/phase-01/week-01/attention.py) and supplied
acceptance tests. Function: `scaled_dot_product_attention(q, k, v, *, causal=False)`.

**Contract:** Q/K/V have identical shape `[B, H, T, D]`, positive dimensions, CPU float32
values, and return a tensor of the same shape. Causal mode permits the current and earlier
positions. Preserve autograd connectivity and do not modify inputs. Validation of unsupported
inputs is outside this first exercise. Exclude padding, dropout, cross-attention, unequal
head dimensions, caching, and fused kernels. Use tensor primitives; calling framework SDPA
or a complete attention layer is allowed in tests as an oracle, not in the learner solution.

**Verification:** shape cases, analytical uniform-score examples, framework agreement,
future-token isolation, a single-token case, unchanged inputs, finite outputs, and finite
gradients agreeing with the reference. CPU comparison tolerances are stated in the tests.

**Expected observations:** causal and noncausal visibility differ; perturbing future data
must not affect earlier causal outputs; floating-point reference agreement uses tolerances.
These are properties to verify, not claims that an implementation has already passed.

## Exercise B: Greedy generation (1 hour)

**Problem/objective:** implement correct generation control flow independently of model
quality. Start from the [generation stub](../../labs/phase-01/week-01/generation.py).

```python
greedy_generate(next_token_logits, prompt_ids, max_new_tokens, *, eos_token_id=None)
```

**Contract:** the prompt is a nonempty list of valid token IDs; the limit is a nonnegative
integer. The supplied callback accepts the full current prefix and returns a finite 1-D
CPU logits tensor with at least one vocabulary entry. Select the highest-scoring token
(first index on a tie). Return a new list containing the original prompt and generated
tokens; never mutate the caller's prompt. Include a newly generated EOS token and stop
immediately after it. An EOS token already in the input prompt does not prevent generation.
A zero limit returns a copy of the prompt without calling the callback. Assume valid inputs.

The deterministic callbacks are supplied by the tests; no model implementation is needed.
For exploration, a callback such as `lambda prefix: torch.tensor([0.0, 2.0, -1.0])` supplies
fixed scores. This callback is a fixture, not a trained language model or a generation-loop
solution. Test full-prefix calls, prompt preservation, token choice, length bounds, zero
limit, EOS inclusion/termination, and default no-EOS behavior.

**Expected observations:** deterministic scores make failures reproducible; bounded loops
stop without requiring natural language output. This interface recomputes over the full
prefix. It is not a KV-cached decode path and is not a performance benchmark.

## Inference trace and explanation (1 hour)

Create `explanation.md` in the lab when ready, in English. Trace two generated tokens from
a short token-ID prompt: callback inputs, next-token scores, chosen tokens, and termination.
Explain which full-prefix work is repeated and what state a later cache might reuse.

Explain prefill versus decode, the roles of model weights/activations/cached state, and the
difference between evaluation mode and disabling gradient recording. Give tensor element
and byte counts for one attention shape with explicit dtype assumptions. Label analytical
estimates as estimates. No latency benchmark is required this week.

## Review and assessment

Ask these interactively after appropriate teaching/practice; do not publish an answer key:

1. Given Q/K/V shaped `[2, 4, 8, 16]`, what are the intermediate attention shapes?
2. Why scale the scores, and along which dimension should softmax operate?
3. How would you demonstrate that the implementation cannot attend to future tokens?
4. Why are `eval()` and disabling gradient recording different?
5. What changes between processing a prompt and generating another token? Which prior
   computations might be reusable?

Add a small masking/dimension debugging case and ask the learner to explain the callback
boundary's trade-offs. The [shared rubric](../../AGENTS.md) covers all applicable dimensions;
record limitations and assistance instead of equating green tests with mastery.

## Deliverables and completion criteria

- Learner-authored attention and generation implementations passing the supplied checks.
- Exact test commands/results and environment/source-state evidence.
- The English explanation described above.
- An interactive assessment record identifying independent work, hints, and remaining gaps.
- Updated progress and handoff, followed by explicit `SIGN OFF: P1.W1` from the learner.

Passing tests is necessary but not sufficient. The learner must explain the implementation
and diagnose a masking/shape error. Keep remaining gaps visible. Do not advance to Week 2
automatically; this module's sign-off does not sign off Phase 1.
