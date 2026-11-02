# Phase 4: Distributed Inference and Training

## Overview

Weeks 13-18; 48-72 hours, target 60. Prerequisites: Phase 3 sign-off, foundations including
autograd, and experience measuring a service. Preserve a substantive training track while
connecting parallelism, communication, memory, and recovery to distributed inference.

Use real local two-process CPU/Gloo execution. Verify backend support when starting; if
the host build lacks Gloo, use a local Linux CPU container. This is not a simulation of
process communication, but it is not evidence of NCCL or multi-GPU performance. Label
analytical TP/PP models and simulations separately. GPU experiments are optional.

## Learning objectives

- **Conceptual:** explain collectives, data/tensor/pipeline parallelism, prefill/decode
  disaggregation, backpropagation, mixed precision, accumulation, FSDP, ZeRO, and recovery.
- **Implementation:** build a small training loop, real CPU DDP, checkpoint/resume, and
  controlled communication/failure experiments.
- **Performance:** estimate weights/gradients/optimizer/activation memory and communication
  costs; analyze synchronization, recomputation, and network bottlenecks.
- **System design:** justify a parallelism strategy, state layout, checkpoint protocol,
  and recovery behavior given hardware and workload constraints.

## Weekly milestones and exercise previews

| Week | Starting point and planned exercise | Verification / expected observation |
| --- | --- | --- |
| 13 | Small multiprocess collective experiments: All-Reduce and All-Gather | Validate values and collective ordering; label local transport costs |
| 14 | TP/PP and distributed-inference cost models; disaggregation | Explain bubbles, transferred state, and network assumptions |
| 15 | Small single-process training task, accumulation, mixed precision analysis | Validate loss/gradients and account for optimizer/activation memory |
| 16 | Adapt the task to two-process CPU DDP | Compare controlled effective batches/updates with a single-process baseline |
| 17 | Analyze FSDP/ZeRO and activation checkpointing | Account for sharded state, added communication, and recomputation |
| 18 | Checkpoint/resume and injected worker failure | Recover model/optimizer/progress state; document failures and assess |

Each week budgets 8-12 hours including study and review. Expand experiments when needed.
Backend capability is verified before execution; do not silently convert a required
multiprocess experiment into a diagram if local setup fails.

## Study materials

Links and relevant topics checked 2026-11-01. Time is included in phase effort.

| Resource | Classification and activity | Hours | Expected takeaway |
| --- | --- | --- | --- |
| [PyTorch distributed overview](https://docs.pytorch.org/tutorials/beginner/dist_overview.html) and [DDP tutorial](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html) | Required; selected reading and adapted CPU experiments | 4 | Understand process groups, synchronized gradients, and distributed training setup |
| [DeepSpeed ZeRO overview](https://www.deepspeed.ai/tutorials/zero/) | Required; reading and state-memory calculations | 1.5 | Distinguish partitioning of optimizer states, gradients, and parameters |
| [NCCL collectives](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html) | Optional hardware depth; reading before a separately planned GPU lab | 1 | Map required collective concepts to GPU communication APIs |

CUDA/NCCL fundamentals remain required conceptual coverage even though actual NVIDIA API
execution is optional. Recheck current FSDP documentation through the PyTorch distributed
material when preparing Week 17; do not assume FSDP supports the chosen CPU setup.

## Key concepts

Track global versus local batch, accumulation steps, gradient reduction semantics, optimizer
state, and RNG/sampler position. Distinguish logical communication volume from measured
transport time. State dtype/precision assumptions in memory estimates. A checkpoint must
restore more than weights if it claims training continuity. Failure recovery is measured
behavior, not an assertion based on saving a file.

## Project 3: Distributed Training Lab

Minimum scope: reproducible small training task, CPU DDP, checkpoint/resume, worker-failure
experiment, tests, and memory/communication report. Project work occupies the six-week
48-72 hour allocation, including conceptual comparisons with distributed inference.

Test controlled single-process/DDP update agreement, data partitioning, checkpoint state,
and resume behavior. Record backend, process count, thread settings, workload, versions,
and observed results. Do not claim deterministic bitwise agreement unless established.
Real GPU FSDP/ZeRO, NCCL profiling, and multi-node scaling are optional extensions requiring
documented hardware; see the [roadmap boundaries](../../ROADMAP.md).

## Industry and research connections

Connect PyTorch process groups/DDP and DeepSpeed ZeRO to communication and state ownership.
Discuss why TP/PP, disaggregation, and sharding trade memory for communication or scheduling
complexity. Local CPU results cannot predict GPU interconnect scaling without more evidence.

## Assessment and sign-off

Explain gradient synchronization, diagnose a mismatched collective, interpret a controlled
DDP comparison, recover training state, and calculate DDP/FSDP/ZeRO memory trade-offs.
Separate conceptual proficiency, CPU execution evidence, simulations, and unverified NVIDIA
skills in the [shared rubric](../../AGENTS.md). After remediation/readiness review, request
`SIGN OFF: Phase 4`; retain gaps and module confirmations explicitly.
