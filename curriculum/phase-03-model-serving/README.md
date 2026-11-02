# Phase 3: Model Serving and Performance

## Overview

Weeks 9-12; 32-48 hours, target 40. Prerequisites: Phase 2 sign-off and a tested inference
engine. Expose inference as a bounded, observable service whose load behavior can be explained.
Use the educational engine and a real local Ollama backend. Choose a small local model and
verify its license, size, and memory needs when starting the phase; no bootstrap download.

## Learning objectives

- **Conceptual:** explain loading/readiness, streaming/SSE, queueing, concurrency,
  backpressure, admission control, cancellation, TTFT, TPOT, and tail latency.
- **Implementation:** build a documented chat API subset, adapters, bounded queues,
  streaming/cancellation, metrics, and a load generator.
- **Performance:** separate queue, prefill, and decode time; measure latency distributions,
  throughput, and capacity with reproducible workloads.
- **System design:** compare vLLM/SGLang components and justify overload/lifecycle behavior.

## Weekly milestones and exercise previews

| Week | Starting point and planned exercise | Verification / expected observation |
| --- | --- | --- |
| 9 | Wrap Project 1; add Ollama adapter, readiness, chat API, SSE | Document supported fields/endpoints and test streaming completion |
| 10 | Add bounded concurrency, admission, cancellation, and backpressure | Overload is controlled; disconnected requests release resources |
| 11 | Instrument and load test the service | Distinguish queue delay from model time; retain raw event evidence |
| 12 | Investigate overload and compare serving architectures | Explain bottlenecks and capacity limits; assess Project 2 |

Each week uses 8-12 hours including review. Expand the API contract and exercises when the
phase starts; compatibility claims must match the tested subset, not an entire vendor API.

## Study materials

Links checked 2026-11-01; API details must be rechecked when implementing the server.

| Resource | Classification and activity | Hours | Expected takeaway |
| --- | --- | --- | --- |
| [vLLM architecture overview](https://docs.vllm.ai/en/latest/design/arch_overview/) | Required; read and draw component boundaries | 1.5 | Relate request handling, scheduling, and model execution |
| [Ollama API](https://docs.ollama.com/api/introduction) | Required; local integration practice | 1.5 | Understand local transport/streaming and adapt it explicitly |
| [SGLang documentation](https://docs.sglang.io/) | Optional; selected architecture/prefix-cache comparison | 1.5 | Compare serving trade-offs without assuming identical hardware support |

## Key concepts

Define metric boundaries before collecting data: client versus server TTFT, inter-token
latencies, TPOT treatment for very short outputs, request versus token throughput, and
percentiles. Transport chunks are not necessarily individual tokens. Record load arrival
pattern, completed/failed/cancelled requests, warm-up, and resource limits.

## Project 2: Mini LLM Server

Minimum scope: educational engine and local Ollama adapters, documented OpenAI-compatible
chat subset, streaming, bounded queues, cancellation, readiness, metrics, and load tests.
The 32-48 hour phase budget includes project implementation, measurement, and assessment.

Test stream endings, malformed supported inputs, disconnect cleanup, queue limits, model
readiness, and backend failure. Deliver setup/API documentation and a reproducible load
report. Broad API compatibility, GPU deployment, and elaborate multi-model orchestration
are optional extensions. Use no cloud endpoints or paid services without approval.

## Industry and research connections

Map our service boundaries to vLLM/SGLang architecture and distinguish a network wrapper
from an inference scheduler. A local backend integration is not a reproduction of a GPU
engine's performance or implementation.

## Assessment and sign-off

Demonstrate lifecycle, streaming, cancellation, and overload behavior; diagnose a concurrency
regression; interpret TTFT/TPOT/tail-latency data; explain capacity and scheduling trade-offs.
Use the [shared rubric](../../AGENTS.md), retain evidence and gaps, then request
`SIGN OFF: Phase 3` after readiness review. Confirm substantial modules separately.
