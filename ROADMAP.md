# AI Infrastructure Roadmap

## Planning baseline

26 relative weeks, 8-12 hours/week: **208-312 hours**, targeting **260 hours**. Reading,
practice, review, assessments, and remediation are included. Optional deep dives consume
spare capacity or extend the schedule. Weeks are estimates, not automatic advancement dates.

The curriculum builds on reported software/distributed systems experience without treating
it as assessed mastery. Verify foundations before accelerating. Preserve broad inference
and training coverage before selecting a specialization. Actual status belongs exclusively
in [PROGRESS.md](PROGRESS.md); this document does not certify completion.

## Phase map

| Phase | Weeks | Hours (target) | Objective and milestone sequence |
| --- | --- | --- | --- |
| [1: Foundations](curriculum/phase-01-foundations/README.md) | 1-4 | 32-48 (40) | Attention/generation -> tiny decoder/autograd -> GPU execution -> roofline/profiling |
| [2: Inference engines](curriculum/phase-02-inference-engines/README.md) | 5-8 | 32-48 (40) | KV cache -> batching/scheduler -> paging/prefix sharing -> optimization analysis |
| [3: Serving and performance](curriculum/phase-03-model-serving/README.md) | 9-12 | 32-48 (40) | API/streaming -> bounded concurrency -> metrics/load -> architecture/overload review |
| [4: Distributed inference and training](curriculum/phase-04-distributed-training/README.md) | 13-18 | 48-72 (60) | Collectives -> TP/PP -> training -> DDP -> sharding -> recovery |
| [5: Platform engineering](curriculum/phase-05-platform/README.md) | 19-22 | 32-48 (40) | Gateway/security -> quotas/reliability -> deployment -> observability |
| [6: Capstone](curriculum/phase-06-capstone/README.md) | 23-26 | 32-48 (40) | Scope/architecture -> integration -> experiments -> demonstration/assessment |

Phase documents own specific resources, reading estimates, weekly milestones, project
boundaries, and completion criteria. Only [P1.W1](curriculum/phase-01-foundations/week-01.md)
is expanded into a detailed executable module at bootstrap. Expand subsequent modules just
in time using the [phase template](curriculum/PHASE_TEMPLATE.md).

## Portfolio progression

1. **Mini Inference Engine (Phase 2):** build on the Phase 1 decoder, adding correct caching,
   batching, bounded scheduling, memory accounting, tests, and benchmarks.
2. **Mini LLM Server (Phase 3):** wrap that engine and a real local backend with streaming,
   cancellation, admission control, metrics, and load tests.
3. **Distributed Training Lab (Phase 4):** retain a separate substantive training project
   covering CPU DDP, checkpoint recovery, communication, and memory analysis.
4. **AI Serving Platform (Phases 5-6):** extend the server into a gateway and integrate
   routing, quotas, reliability, observability, reproducible deployment, and a final demo.

Project-specific effort is included in its phase allocation. Do not create all project
directories or implementations in advance. Functional educational scope comes first;
production extensions are explicitly optional.

## Hardware and assessment boundaries

The baseline is locally achievable with CPU and optional Apple Silicon acceleration.
Training uses genuine local multiprocess CPU execution; simulated parallelism and analytical
cost models must be labeled. NVIDIA execution skills remain unverified without real hardware.

Optional CUDA/Triton work requires a supported NVIDIA GPU and matching Linux/driver/toolchain;
tiny kernel examples need one device. An actual multi-GPU NCCL/parallel training experiment
needs at least two supported GPUs, with memory sized to the chosen model. Multi-node network
measurements additionally need multiple machines and a documented interconnect. Specify
model, memory budget, versions, duration, and spending before proposing a concrete paid lab.
Never provision paid resources without explicit approval.

Each phase normally requires the previous phase's explicit user sign-off. Each substantial
module and phase receives an interactive assessment with the rubric in [AGENTS.md](AGENTS.md),
supported by implementation, explanation, debugging, design, and performance evidence as
appropriate. The learner may accept documented gaps; sign-off remains distinct from mastery.
Do not advance on the basis of a schedule or green tests alone.

## Adaptation and revision history

Explain major changes before applying them; record their reason, impact, and user decision.
Preserve completed work, original broad objectives, assessment history, and open gaps.
After broad exposure, compare inference, GPU/kernel, distributed systems, training, and
platform specializations using observed interests and demonstrated work.

| Date | Revision | Basis |
| --- | --- | --- |
| 2026-11-01 | Initial 26-week baseline and agent-independent continuity | User-approved setup plan; tensor familiarity is self-reported; optional NVIDIA hardware track |
