# Phase 2: LLM Inference Engines

## Overview

Weeks 5-8; 32-48 hours, target 40. Prerequisites: Phase 1 sign-off, a tested tiny decoder,
and attention/memory reasoning. The purpose is to make inference more efficient while
preserving outputs and explaining workload-dependent trade-offs. Use CPU/PyTorch and
optional MPS; external inference courses are references, not installation dependencies.

## Learning objectives

- **Conceptual:** explain KV caching, batching, scheduling, PagedAttention, prefix sharing,
  quantization, and speculative decoding.
- **Implementation:** extend the tiny decoder with cache state, static/continuous batching,
  request lifecycle, and bounded memory accounting.
- **Performance:** compare cached/uncached execution and throughput/latency under controlled
  workloads; reason about capacity, fragmentation, precision, and acceptance overhead.
- **System design:** justify admission and scheduling policies, cache isolation and reuse,
  and the limits of simplified paging models.

## Weekly milestones and exercise previews

| Week | Starting point and planned exercise | Verification / expected observation |
| --- | --- | --- |
| 5 | Extend Phase 1 decoder with a KV cache | Cached/uncached logits agree; separate saved computation from added state |
| 6 | Add static then continuous request scheduling | Mixed lengths complete without corruption; reason about idle slots and fairness |
| 7 | Add memory budgeting and a simplified paged-cache/prefix-sharing model | Capacity is enforced, cache ownership is isolated, sharing is valid only for matching prefixes |
| 8 | Analyze quantization/speculative decoding; benchmark core engine | Record actual results and explain accuracy, acceptance, and overhead trade-offs |

Budget 8-12 hours per week. Expand requirements and tests just in time; no future solutions
are supplied. Do not infer that paging, quantization, or speculative decoding always helps.

## Study materials

Links/sections checked 2026-11-01. Reading time is part of phase effort.

| Resource | Classification and activity | Hours | Expected takeaway |
| --- | --- | --- | --- |
| [PagedAttention paper](https://arxiv.org/abs/2309.06180) | Required; read memory-management motivation/design and draw a block layout | 2 | Connect fragmentation, sharing, and serving capacity |
| [tiny-llm](https://github.com/skyzh/tiny-llm), cache and batching material | Required; selected source/lesson inspection, record inspected revision | 2 | Compare Apple Silicon inference code with our engine; some sections are evolving |
| [mini-sglang](https://github.com/sgl-project/mini-sglang) | Optional; guided scheduler/memory source inspection | 2 | Compare a compact serving design with the educational scheduler |

## Key concepts

Account separately for weights, live activations, and cached keys/values. A basic cache
estimate is `2 * layers * batch * tokens * KV_heads * head_dim * bytes_per_element`, with
explicit assumptions about layout and attention type. Track allocation versus useful
tokens, scheduling fairness, prefix identity, quantization error, and speculative acceptance.

## Project 1: Mini Inference Engine

Minimum scope: tiny decoder, correct cache, static and continuous batching, bounded request
scheduling/memory accounting, tests, benchmark scripts, and documented limitations. Project
work spans these four weeks within the 32-48 hours. Reuse Phase 1 rather than duplicate it.

Required tests cover cached/uncached equivalence, cache isolation, mixed lengths, admission
limits, and request completion. Benchmark controlled input/output lengths and concurrency
with environment/methodology evidence. A simulated paged allocator is not an optimized GPU
paged-attention kernel. Optimized kernels and production speculative decoding are extensions.

## Industry and research connections

Use the PagedAttention paper to connect virtual-memory ideas to KV storage. Compare actual
source from tiny-llm/mini-sglang without inheriting their whole scope or copying reference
solutions. Published performance claims are not results for this repository.

## Assessment and sign-off

Demonstrate correctness under mixed request lengths and memory pressure, interpret a
throughput/latency comparison, diagnose cache contamination, and explain when each major
optimization might lose. Record evidence with the [shared rubric](../../AGENTS.md), remediate
gaps, then request `SIGN OFF: Phase 2`. Module checkpoints also require explicit confirmation.
