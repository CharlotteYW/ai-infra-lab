# P1.W1 Learner Lab

Follow the [curriculum module](../../../curriculum/phase-01-foundations/week-01.md) for the
learning sequence, contracts, resources, and assessment. The agent supplied the stubs and
acceptance tests. You supply the implementations and independent explanation.

## Run from the repository root

```sh
uv sync --locked
uv run --locked pytest -m environment -v -s
uv run --locked pytest --collect-only -q
uv run --locked pytest -m exercise -v --tb=short
```

At bootstrap, exercise tests fail with `NotImplementedError`. This means the exercises
are unfinished; they are not hidden behind skips or expected-failure markers. Environment
checks establish setup readiness only. An unfiltered test run includes both groups.

To focus on one exercise:

```sh
uv run --locked pytest labs/phase-01/week-01/tests/test_attention.py -v --tb=short
uv run --locked pytest labs/phase-01/week-01/tests/test_generation.py -v --tb=short
uv run --locked ruff check .
uv run --locked ruff format --check .
```

## Work sequence

1. Answer the short diagnostic with your mentor before receiving a solution.
2. Work through a small example, then implement `attention.py` using tensor primitives.
3. Read test failures, explain their meaning, and request progressive hints as needed.
4. Implement `generation.py` around the supplied deterministic callback contract.
5. Create `explanation.md` here after attempting the exercises; see the module requirements.
6. Record actual commands and evidence for review and interactive assessment.

Framework SDPA in the tests is an oracle, not the learner implementation. Tests use valid
CPU float32 inputs and do not require MPS, downloaded weights, network access, or a model
server. The exercise scope deliberately excludes defensive validation of unsupported inputs.

Never rewrite tests merely to hide unfinished or incorrect work. Discuss genuine test
defects with evidence. Do not infer sign-off or mastery from a passing test run.
