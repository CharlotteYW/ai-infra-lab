# Phase 1: AI Infrastructure Foundations

## Overview

Weeks 1-4; 32-48 hours, target 40, including review and assessment. Translate familiar
systems reasoning into Transformer computation, memory traffic, and GPU execution.
Prerequisites: Python and reported tensor familiarity; diagnose linear algebra, autograd,
and attention rather than assuming mastery. No earlier sign-off is required.

Use Python/PyTorch on CPU; MPS is optional after capability checks. CUDA/Triton source
walkthroughs require no NVIDIA device. Actual CUDA execution is an optional separate lab.

## Learning objectives

- **Conceptual:** explain tokenization, attention, causal masking, Transformer forward
  computation, autoregressive generation, prefill/decode, and computational graphs.
- **Implementation:** implement attention, a generation loop, and later a tiny decoder;
  use autograd and appropriate inference behavior.
- **Performance:** estimate parameters/activations/cache memory, FLOPs, memory traffic,
  arithmetic intensity, and roofline limits; interpret a measured profile.
- **System design:** distinguish CPU/GPU execution, memory hierarchies, kernel launches,
  coalescing, and compute-versus-bandwidth constraints without equating MPS with CUDA.

## Weekly milestones

| Week | Planned work | Evidence |
| --- | --- | --- |
| 1 | [Transformer and inference fundamentals](week-01.md) | Attention/generation tests and independent explanations |
| 2 | Tiny decoder, parameters/activations, gradients, evaluation/inference modes | Forward/gradient checks and a computation trace |
| 3 | GPU execution/memory, CUDA fundamentals, guided Triton kernel reading | Execution/memory diagram and coalescing reasoning |
| 4 | FLOPs, bandwidth, arithmetic intensity, roofline, profiling | Reproducible CPU/optional MPS experiment and assessment |

## Study materials

Source links and listed sections were checked during planning on 2026-11-01. Times are
estimates included in the phase budget, not additional coursework.

| Resource | Classification and activity | Hours | Expected takeaway |
| --- | --- | --- | --- |
| [D2L Transformer chapter](https://d2l.ai/chapter_attention-mechanisms-and-transformers/transformer.html), with linked Q/K/V, scoring, multi-head, and positional-encoding sections | Required; selected reading and shape tracing | 3 | Relate attention equations and residual blocks to model data flow; distinguish encoder-decoder examples from decoder-only LLMs |
| [PyTorch Autograd](https://docs.pytorch.org/tutorials/beginner/introyt/autogradyt_tutorial.html) | Required; reading and small experiments | 1 | Explain graph construction, gradients, and inference behavior |
| [PyTorch SDPA](https://docs.pytorch.org/tutorials/intermediate/scaled_dot_product_attention_tutorial.html), basic usage and causal self-attention | Required; selected reading and reference comparisons after first attempt | 1 | Connect framework behavior to the learner's attention implementation |
| [CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/), Introduction and Programming Model | Required; reading and execution diagram | 1.5 | Explain GPU execution and memory organization |
| [Triton tutorials](https://triton-lang.org/main/getting-started/tutorials/index.html), Vector Addition and Fused Softmax | Optional deeper reading beyond the guided Week 3 walkthrough | 2 | Explain tiling, memory access, and fusion motivation; execution needs compatible hardware |

## Key concepts

Track tensor shapes and units alongside formulas. Topics include scaled dot-product
attention, causal visibility, multi-head projection, residual/norm/MLP roles, token IDs,
logits, parameter bytes, activation storage, and reusable inference state. Later distinguish
FLOPs from FLOP/s; arithmetic intensity is FLOPs/bytes and a roofline estimate is bounded by
both compute capacity and bandwidth times arithmetic intensity. State all workload assumptions.

## Exercises and consolidation

Week 1 is fully specified in its module. Weeks 2-4 remain previews, expanded only when
needed: build a tiny decoder from Week 1 primitives; trace a graph and memory allocation;
read a kernel and predict memory access; then test a compute/bandwidth hypothesis using
small local experiments. Each week budgets 8-12 hours across reading, practice, and review.

No separate portfolio project is necessary in this phase. Its tested decoder and reports
form the starting point for Project 1. Do not download a large model or implement a full
training framework to complete foundations.

## Industry and research connections

Compare the educational attention operator with PyTorch's SDPA interface, without assuming
an identical kernel or performance profile. Use CUDA/Triton examples to connect memory
traffic and kernel fusion to model execution; local MPS results are not CUDA benchmarks.

## Assessment and sign-off

Required evidence: attention/decoder correctness, an independent Transformer/prefill/decode
explanation, a justified memory estimate, and a measured performance report. Diagnose a
masking/shape issue and identify a compute or memory bottleneck with stated assumptions.
Explain the limits of the experiment, including any device work not executed.

Apply the shared rubric in [AGENTS.md](../../AGENTS.md). Remediate gaps, recommend readiness,
then request `SIGN OFF: Phase 1`. Week 1 has its own `P1.W1` checkpoint and does not sign off
the phase. Store actual evidence and confirmations in assessments/progress.
