# Bootstrap Engineering Verification

Date: 2026-11-01 (America/Los_Angeles).
Reviewer: Codex, acting as the repository scaffolding assistant.

**This is an engineering verification record, not a learner assessment or sign-off.**
The learner has not answered the diagnostic or implemented the exercises. No concepts
were assessed and no module/phase completion is implied.

## Scope and observed environment

Created the agent-independent state files, six phase overviews, Week 1 specification,
assessment/phase templates, learner stubs, tests, and locked local environment. The source
directory was empty before bootstrap. Git was initialized on `main`; no commit, remote,
or push was made. All files remain uncommitted.

| Item | Observed value |
| --- | --- |
| Hardware | Apple M5 Pro, arm64, 64 GiB memory |
| OS | macOS 27.2, build 26B123 |
| Python | 3.11.15 |
| PyTorch | 2.15.0 |
| NumPy | 2.4.6 |
| pytest / Ruff | 9.2.0 / 0.17.3 |
| MPS | Built and available; a small matrix operation executed successfully |
| Docker / Ollama / GPU experiments | Not exercised; executable availability is not service readiness |

## Commands actually executed and final outcomes

Run commands from the repository root. These results refer to the source hashes below.

| Command | Actual outcome |
| --- | --- |
| `git init -b main` | Initialized local repository |
| `uv lock` | Resolved and wrote the dependency lockfile; rerun after adding NumPy |
| `uv sync --locked` | Installed the locked project/development environment |
| `uv run --locked pytest -m environment -v -s` | 4 passed, 22 deselected; final fresh-environment run had no warnings |
| `uv run --locked pytest --collect-only -q` | 26 tests collected without collection errors or warnings in the final run |
| `uv run --locked pytest -m exercise -q --tb=no --junitxml=/tmp/ai-infra-lab-bootstrap-exercises.xml` | Exit 1: 22 failed, 4 deselected; all failures are the intended stub `NotImplementedError` |
| `uv run --locked ruff check .` | Passed after fixing two line-length issues |
| `uv run --locked ruff format .` | Reformatted two test files |
| `uv run --locked ruff format --check .` | Passed |
| `git branch --show-current` / `git remote -v` | `main`; no remotes |
| `git rev-parse --verify HEAD` | Nonzero exit confirms there is no initial commit |

The earlier exercise run used `uv run --locked pytest -m exercise -q --tb=short
--junitxml=/tmp/ai-infra-lab-bootstrap-exercises.xml` and also failed at all 22 explicit
stubs. JUnit inspection confirmed 22 failures, zero collection/runtime errors reported as
JUnit errors, zero skipped exercises, and the expected `NotImplementedError` messages.
The `/tmp` XML is a disposable diagnostic artifact; the durable outcome is retained here.

An initial PyTorch import emitted a missing-NumPy warning. Added NumPy as an explicit
runtime dependency, regenerated the lockfile, and reran collection, exercise checks,
and environment verification. The final runs emitted no warnings. No warning was suppressed.

### Fresh environment reproduction

This exact wrapper was executed successfully. It installed the locked dependencies in a
new temporary environment, ran the environment checks, then removed only that temporary
directory. Dependency downloads could use the existing `uv` cache; this was not an offline
or clean-download test.

```sh
python3 - <<'PY'
import os
from pathlib import Path
import subprocess
import tempfile
with tempfile.TemporaryDirectory(prefix='ai-infra-lab-clean-') as directory:
    environment = os.environ.copy()
    environment['UV_PROJECT_ENVIRONMENT'] = str(Path(directory) / 'venv')
    for command in (
        ['uv', 'sync', '--locked'],
        ['uv', 'run', '--locked', 'pytest', '-m', 'environment', '-v', '-s'],
    ):
        print('Running in a fresh temporary environment:', ' '.join(command), flush=True)
        subprocess.run(command, env=environment, check=True)
print('Fresh environment verification passed; temporary environment removed.')
PY
```

### Documentation and continuity audit

Standard-library checks resolved repository-relative Markdown links, checked Markdown
trailing whitespace, and verified all six phase overviews retain the required objective
categories and assessment sections. Manual review checked project boundaries, resource
classifications, sign-off gates, and separation of future plans from actual progress.

Read the four state files as a repository-only resume check: the active position is P1.W1
planned/not started; latest sign-off is none; the diagnostic and both learner exercises
are pending; G-001 through G-004 remain open; the next action is the tensor-shape diagnostic.
No separate agent was invoked and no private memory is required to recover this state.

Ignore-policy checks verified that environments, caches, `.env` files, downloaded models,
large artifact directories, and checkpoint/weight files are ignored. Small evidence under
`assessments/` and `benchmarks/`, plus `.env.example`, are not ignored.

## Source identification (SHA-256)

No commit exists. These hashes identify the tested runtime configuration and Python sources;
later work should not treat this record as evidence for modified implementations.

| Path | SHA-256 |
| --- | --- |
| `.python-version` | `db82937e1f1830581a9553c7814f5c5fcacb6dfdef8310b43e9a812c887acaf5` |
| `pyproject.toml` | `190873f3b64fa8631a014747a60888d0124deb333982db4cc81c512822d33976` |
| `uv.lock` | `63822d432311fc2a1f664e80756e8e450a9417decf426ba0053358b33c5ee779` |
| `labs/phase-01/week-01/attention.py` | `fd6bf8cb42a926406d23749e995090220a1029ddc807e08e8ae321756cd0a877` |
| `labs/phase-01/week-01/generation.py` | `250fe2ef1f4c9ae6c240a3caceeb37d7b359b27927d13ca133f9148d670dafac` |
| `labs/phase-01/week-01/tests/test_attention.py` | `9aaf4a9ddcb667aa1398dd26ed62c360110d085fcaedf4bc1f91511b9378c952` |
| `labs/phase-01/week-01/tests/test_environment.py` | `df89dfc553d68c6a578a3ba79c6fbe9fe6d1abd7c33d0e6b535f1abd6571d438` |
| `labs/phase-01/week-01/tests/test_generation.py` | `ea64e7bfdb1ed2449dda4893598c9e326195ca541ea3f67ad542dbe13fe49167` |

## Limits and next action

No inference benchmark was executed, no learning exercise was solved, and no learner
assessment or sign-off occurred. The 22 failing checks demonstrate unfinished stubs, not
learner weakness. CUDA/NCCL practical ability remains unverified.

Next: ask the first diagnostic question in
[P1.W1](../curriculum/phase-01-foundations/week-01.md), wait for the answer, and adapt the
lesson. State and unresolved gaps are in [PROGRESS.md](../PROGRESS.md).
