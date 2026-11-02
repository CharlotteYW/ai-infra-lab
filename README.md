# AI Infrastructure Learning Lab

A personal learning repository and engineering portfolio for understanding, implementing,
measuring, and explaining AI infrastructure. The baseline spans 26 weeks at 8-12 hours
per week and includes foundations, inference, serving, distributed systems, training,
platform engineering, and an integrated capstone.

The learner owns learning decisions and sign-offs. Any assistant can mentor from the
repository without prior conversations or private memory.

## Start here

- [Roadmap](ROADMAP.md): planned phases, milestones, and project sequence.
- [Progress](PROGRESS.md): actual learning status and unresolved work.
- [Session handoff](SESSION_HANDOFF.md): latest context and exact next action.
- [Mentoring contract](AGENTS.md): rules for every assistant.
- [Week 1](curriculum/phase-01-foundations/week-01.md): first learning module.
- [Assessment template](assessments/TEMPLATE.md): evidence and user-controlled sign-off.

The initial repository contains phase overviews and Week 1 learner stubs/tests. Future
projects are planned, not implemented. Current execution and learning status live in the
progress and handoff files, not in this introduction.

## Resume with any assistant

Copy this instruction into a new session, including with agents that do not automatically
read `AGENTS.md`:

> Read AGENTS.md, ROADMAP.md, PROGRESS.md, and SESSION_HANDOFF.md. Inspect the relevant
> source, Git status/recent changes, and referenced assessments/sign-offs. Summarize the
> current module, latest user sign-off, pending exercises, gaps, and blockers. Recommend
> the next small action. Resolve conflicting records with me before changing disputed
> state. Do not infer understanding from working code or advance without my sign-off.

## Local setup

Use a terminal in the repository root. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
if it is not already available. Python 3.11.15 is selected by `.python-version`; `uv` can
download it if missing. The lockfile pins dependencies; no model downloads, API keys,
Docker service, or paid resources are needed for Week 1.

```sh
uv sync --locked
uv run --locked pytest -m environment -v -s
uv run --locked ruff check .
uv run --locked ruff format --check .
```

The environment checks report Python/PyTorch/platform and MPS capability, execute CPU
tensor operations and autograd, and run a small MPS operation only when available.
MPS absence is a reported skip; CPU is the required Week 1 target. These checks establish
environment readiness, not learner understanding or benchmark performance.

```sh
uv run --locked pytest --collect-only -q
uv run --locked pytest -m exercise -v --tb=short
```

**Exercise tests deliberately fail with `NotImplementedError` until you implement the
learner stubs.** They are not skipped or marked as expected failures. An unfiltered
`pytest` run includes them and therefore also fails initially. Passing setup checks does
not complete an exercise. See the [lab instructions](labs/phase-01/week-01/README.md).

Dependency upgrades are deliberate: review the proposed change, regenerate the lockfile,
and rerun the checks. Normal sessions use `--locked` so an environment is not silently
re-resolved. Python upgrades also require updating the runtime pin and project constraint.

## Organization and portfolio

`curriculum/` contains specifications and resources; `labs/` contains small learning
exercises. Create `projects/` and `benchmarks/` when the first substantive work belongs
there. Keep project explanations and compact evidence beside the corresponding work.

| Planned project | Phase | Minimum purpose |
| --- | --- | --- |
| Mini Inference Engine | 2 | Correct caching, batching, scheduling, and memory accounting |
| Mini LLM Server | 3 | Streaming, bounded concurrency, cancellation, and measurement |
| Distributed Training Lab | 4 | Local DDP, recovery, and communication/memory analysis |
| AI Serving Platform | 5-6 | Routing, limits, reliability, observability, and integration |

CPU and optional MPS experiments form the portable baseline. The learner also reports a
local NVIDIA RTX 3090 and can rent cloud GPUs for suitable experiments. See the
[hardware inventory](PROGRESS.md#available-hardware-and-compute) for verification status
and spending boundaries. Simulations never stand in for genuine hardware evidence.

## GitHub connection

Public repository: [CharlotteYW/ai-infra-lab](https://github.com/CharlotteYW/ai-infra-lab).
Local `main` tracks `origin/main`; the SSH remote is
`git@github.com:CharlotteYW/ai-infra-lab.git`. Initial publication was explicitly authorized
by the learner on 2026-11-01. Repository content and commit messages are English.

Follow the authorization rules in [AGENTS.md](AGENTS.md) for future external actions.
No GitHub account, agent plugin, or hosted service is needed to continue learning locally.
