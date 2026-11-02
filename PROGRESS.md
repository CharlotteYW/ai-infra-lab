# Actual Learning Progress

Updated: 2026-11-01 (America/Los_Angeles).

## Current state

- Setup: complete and verified; this is an engineering milestone, not a learning sign-off.
- Learning position: Phase 1 / P1.W1 is planned; learning has not started.
- Most recent signed-off milestone: none.
- Assessments completed: none.
- Demonstrated skills: none assessed in this repository.
- Background: experienced backend/distributed/data/ML infrastructure engineer; comfortable
  with tensors. These are learner self-reports, not evaluated achievements.
- Baseline decision: local CPU/optional MPS; NVIDIA hardware practice is optional and
  remains unverified until executed.

## Milestone status

| Milestone | Actual status | Evidence / sign-off |
| --- | --- | --- |
| Repository bootstrap | Complete | [Engineering verification](assessments/2026-11-01-bootstrap-verification.md); no learning sign-off |
| P1.W1 diagnostic | Not started | None |
| P1.W1 attention exercise | Not started; agent-authored stub | No learner implementation |
| P1.W1 generation exercise | Not started; agent-authored stub | No learner implementation |
| P1.W1 explanation and assessment | Not started | None |
| Phase 1 | Not started | No user sign-off |
| Phases 2-6 | Not started | No user sign-offs |

## Available hardware and compute

Hardware inventory updated from the learner's report on 2026-11-01:

| Resource | Availability and verification |
| --- | --- |
| Apple Silicon Mac, 64 GiB unified memory | Existing development environment; CPU/autograd and a small MPS operation verified during bootstrap |
| Local NVIDIA RTX 3090 GPU | Learner reports access; host OS, GPU count, VRAM, driver, CUDA toolkit, framework compatibility, and access method have not been inspected |
| Rented cloud GPUs | Learner is willing and able to rent GPU resources when useful; no provider, GPU configuration, budget, duration, or active instance has been selected |

Prefer the existing local GPU for suitable CUDA experiments after verifying its environment.
Use rental proposals for hardware needs not met locally, such as genuine multi-GPU work.
Each paid experiment still requires explicit approval of its configuration and spending;
availability is not authorization to provision. No CUDA/NCCL experiment has been executed.

## Open questions and verification gaps

These are unassessed areas, not established weaknesses.

| ID | Area | Status / next evidence |
| --- | --- | --- |
| G-001 | Attention tensor shapes, scaling, and masking | Unassessed; Week 1 diagnostic and exercise |
| G-002 | Autograd and inference/evaluation behavior | Unassessed; explanation and debugging question |
| G-003 | Transformer data flow, prefill/decode, reusable state | Unassessed; trace and independent explanation |
| G-004 | CUDA/NCCL and multi-GPU practical ability | Unverified; local RTX 3090 access is reported, but environment and practical skills remain untested |

No known learning blocker. CPU/autograd and a small MPS operation passed environment checks;
the locked setup also passed in a fresh temporary environment. Both learner exercises are
still unimplemented (22 explicit stub failures, not evidence of learner ability).
Keep new durable gaps here with assessment links; close them only against evidence.

## Next action

Begin the short P1.W1 diagnostic by asking:
"Given Q, K, and V shaped [2, 4, 8, 16], what are the intermediate attention shapes?"
Wait for the learner's answer and adapt the lesson to observed gaps.

## Version control

The learner authorized committing existing changes and creating the public repository
[CharlotteYW/ai-infra-lab](https://github.com/CharlotteYW/ai-infra-lab). Initial commit
`db99735` contains the bootstrap; `93592c8` records publication authorization and the
English language confirmation. Both were pushed successfully. Local `main` tracks
`origin/main`; the configured remote is `git@github.com:CharlotteYW/ai-infra-lab.git`.
Repository content and commit messages remain English; conversation may be Chinese or English.

The university-resource integration remains a proposal: the suggested 272.5-hour target
and the 260-hour alternative have not been applied or selected explicitly.

## Record links

- [Curriculum plan](ROADMAP.md)
- [Current module](curriculum/phase-01-foundations/week-01.md)
- [Latest session context](SESSION_HANDOFF.md)
- [Assessment template](assessments/TEMPLATE.md) (template only; no assessment exists)
- [Bootstrap engineering verification](assessments/2026-11-01-bootstrap-verification.md)
  (environment/test evidence only; no learner assessment or sign-off)
