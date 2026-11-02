# Session Handoff

Session: 2026-11-01 (America/Los_Angeles).

## Current state

- Repository bootstrap complete. Phase 1 / P1.W1 planned; learning has not started.
- Most recent module/phase sign-off: none. No learner assessment has occurred.
- Local Git branch: `main`; bootstrap committed as `db99735`. No remote is configured;
  push is pending the learner's destination/visibility selection.

## Completed work and files

- Created `AGENTS.md`, `README.md`, `ROADMAP.md`, `PROGRESS.md`, and this handoff.
- Added six phase overviews, the phase template, and detailed P1.W1 curriculum under
  `curriculum/`; later phases remain plans, not implemented projects.
- Added attention/generation learner stubs, lab instructions, and environment/exercise
  tests under `labs/phase-01/week-01/`. Both learner stubs remain unimplemented.
- Added `.python-version`, `pyproject.toml`, `uv.lock`, `.gitignore`, the assessment
  template, and [bootstrap engineering evidence](assessments/2026-11-01-bootstrap-verification.md).

## Verification actually executed

- `uv lock` and `uv sync --locked`: succeeded; Python 3.11.15 / PyTorch 2.15.0.
- `uv run --locked pytest -m environment -v -s`: 4 passed, including CPU/autograd and
  optional MPS execution. Also passed in a fresh temporary environment without warnings;
  the exact wrapper is in the engineering evidence record.
- `uv run --locked pytest --collect-only -q`: 26 tests collected.
- `uv run --locked pytest -m exercise -q --tb=no --junitxml=/tmp/ai-infra-lab-bootstrap-exercises.xml`:
  22 failures at the intentional learner stubs; 4 environment tests deselected.
- `uv run --locked ruff check .` and `uv run --locked ruff format --check .`: passed after
  formatting two test files. Local-link, phase-outline, and ignore-policy checks passed.
- Benchmarks: not run. Docker/Ollama services and CUDA/NCCL hardware: not exercised.

## Decisions and unresolved learning state

The learner authorized committing and pushing existing changes. After clarifying a typo,
the learner confirmed English repository content AND English commit messages; conversation
may be Chinese or English. The existing language rule in `AGENTS.md` already matches.

Publication work: staged/reviewed all 25 bootstrap files, ran `git diff --cached --check`,
`uv run --locked ruff check .`, and `uv run --locked ruff format --check .` successfully.
A staged-file check found no common credential patterns or unexpected large/generated files.
Created commit `db99735` with message "Initialize AI infrastructure learning lab and
continuity protocol". GitHub CLI is authenticated as `CharlotteYW`; inspection found no
`CharlotteYW/ai-infra-lab` repository. Asked whether to create it private/public or use an
existing URL. Do not choose visibility or create a remote repository until that answer.
This note/progress update will be committed separately to preserve the publication state.
No tests or benchmarks beyond the listed style/staging checks were rerun in this session;
the earlier bootstrap verification remains historical evidence.

The resource-integration review proposed CS224N 2026 materials/2024 public videos, CS336
2026, MIT 6.5940, GPU MODE, supplementary CMU/FSDL, and targeted textbook/repository readings.
Required source time would rise from 25 to 37.5 hours; preserving practice gives a 272.5-hour
target, with a 260-hour alternative replacing mentor-led exposition. No curriculum files
were edited for that proposal; confirm the budget choice before applying it. Preserve
course-specific assignment policies, especially CS336's restrictions on agent assistance.

Use locked Python 3.11 with CPU float32 for Week 1. MPS is available but optional. NumPy
was added to resolve an observed PyTorch import warning. Keep environment tests separate
from unfinished exercise tests; no hidden expected failures and no supplied solutions.
Keep the six-week training phase and explicitly unverified NVIDIA hardware skills.

Learner understanding: not assessed; no demonstrated concepts to record. Tensor familiarity
is self-reported. G-001 through G-004 remain open in [PROGRESS.md](PROGRESS.md). No known
learning blocker. No sign-off or curriculum advancement occurred during setup.

## Exact next action

Begin the short [P1.W1 diagnostic](curriculum/phase-01-foundations/week-01.md) by asking:
"Given Q, K, and V shaped [2, 4, 8, 16], what are the intermediate attention shapes?"
Wait for the learner's answer and adapt the first lesson to observed gaps.
