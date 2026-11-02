# Phase 6: AI Serving Platform Capstone

## Overview

Weeks 23-26; 32-48 hours, target 40. Prerequisites: Phase 5 sign-off and the earlier engine,
server, training lab evidence, and gateway increment. Integrate a reproducible portfolio
project and demonstrate independent systems reasoning. The training project remains part
of the portfolio even though this capstone centers on serving.

At least one real local inference backend is required alongside the educational engine.
Reuse local CPU/MPS/Ollama and control-plane deployment from prior phases. No GPU/cloud
integration is required for baseline completion.

## Learning objectives

- **Conceptual:** explain end-to-end request flow and interactions among model execution,
  routing, streaming, admission, limits, observability, and recovery.
- **Implementation:** integrate the prior projects with clear adapters, documented setup,
  representative tests, and a reproducible demonstration.
- **Performance:** run honest load/failure experiments, retain compact raw evidence, and
  explain bottlenecks and workload-dependent reliability/performance trade-offs.
- **System design:** defend scope, architecture, failure policies, deployment choices,
  limitations, and realistic next improvements.

## Weekly milestones and exercise previews

| Week | Starting point and planned exercise | Verification / expected observation |
| --- | --- | --- |
| 23 | Review Phase 5 increment; freeze minimum scope and workloads | Agree architecture and measurable acceptance criteria before expansion |
| 24 | Integrate gateway, educational engine, and real local backend | Trace representative streaming/non-streaming requests end to end |
| 25 | Run load, cancellation, overload, failure, and recovery experiments | Retain actual measurements and diagnose the observed behavior |
| 26 | Documentation, independent demo, assessment, readiness report | Another engineer can reproduce the demo; learner defends trade-offs |

Budget 8-12 hours/week. Exact workload sizes and performance targets are chosen from the
working system in Week 23, not fabricated during bootstrap. No universal speed target.

## Study materials

Reuse the implementation resources in [Phase 3](../phase-03-model-serving/README.md) and
[Phase 5](../phase-05-platform/README.md): required targeted review, approximately 2 hours,
to resolve integration details rather than introduce another framework. Links were checked
2026-11-01 and should be refreshed for the actual dependency versions.

Optional: [Kubernetes probe guidance](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/),
approximately 1 hour of reading and deployment review. Expected takeaway: distinguish
startup, readiness, and liveness behavior and avoid inappropriate restart policies.

## Key concepts

Keep the critical path, state ownership, resource bounds, API compatibility scope,
observability boundaries, retry behavior, and recovery guarantees explicit. Separate
measured results from design goals and extrapolations. Identify which claims apply only
to the tested local workload and which would require GPU or multi-node validation.

## Project 4, final increment: AI Serving Platform

Minimum scope: educational and real local inference adapters; routing; streaming; rate
limits and bounded admission; reliability policies; metrics/traces; deployment and
architecture documentation; reproducible benchmark and failure reports. Reuse the Phase 5
increment. This phase adds 32-48 hours, giving Project 4 a two-phase 64-96 hour envelope
including study, platform exercises, assessment, and integration.

Test end-to-end requests, disconnect cleanup, overload, backend failure, and recovery.
Record software/hardware, code state, input/output lengths, concurrency, warm-up,
synchronization, repetitions, failure counts, and compact raw evidence. Preserve known
limitations. GPU adapters and advanced orchestration remain optional extensions.

## Industry and research connections

Compare the result with selected vLLM/SGLang serving and Kubernetes/Ray deployment patterns
studied earlier. Explain why an educational platform is not automatically production-ready.
Relate operational failure and recovery reasoning back to the distributed training lab.

## Assessment and sign-off

Another engineer must be able to follow the local demonstration. The learner must explain
request flow, diagnose an injected failure, interpret measurements, defend architecture,
and identify limitations independently. Use the [shared rubric](../../AGENTS.md), retain
remaining gaps, and request `SIGN OFF: Phase 6` only after review and remediation.

After explicit sign-off, propose specialization choices using evidence from the whole
portfolio. Do not erase unresolved NVIDIA or other learning gaps at curriculum completion.
