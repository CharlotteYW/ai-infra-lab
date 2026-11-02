"""Deterministic model callbacks test control flow, not language-model quality."""

import pytest
import torch
from generation import greedy_generate

pytestmark = pytest.mark.exercise


def test_full_prefix_calls_prompt_preservation_and_token_limit() -> None:
    prompt = [4, 1]
    calls: list[list[int]] = []
    scripted_tokens = [2, 3, 0]

    def next_logits(prefix: list[int]) -> torch.Tensor:
        calls.append(list(prefix))
        scores = torch.full((5,), -10.0)
        scores[scripted_tokens[len(calls) - 1]] = 10.0
        return scores

    result = greedy_generate(next_logits, prompt, 3)
    assert result == [4, 1, 2, 3, 0]
    assert calls == [[4, 1], [4, 1, 2], [4, 1, 2, 3]]
    assert prompt == [4, 1]
    assert result is not prompt


def test_generated_eos_is_included_and_stops_callback_calls() -> None:
    calls: list[list[int]] = []

    def next_logits(prefix: list[int]) -> torch.Tensor:
        calls.append(list(prefix))
        assert len(calls) <= 2, "The callback must not be called after generating EOS."
        return torch.tensor([0.0, 5.0, 1.0]) if len(calls) == 1 else torch.tensor([0.0, 1.0, 5.0])

    assert greedy_generate(next_logits, [0], 8, eos_token_id=2) == [0, 1, 2]
    assert len(calls) == 2


def test_first_generated_token_can_be_eos() -> None:
    calls = 0

    def next_logits(prefix: list[int]) -> torch.Tensor:
        nonlocal calls
        calls += 1
        assert prefix == [0]
        return torch.tensor([-1.0, 3.0])

    assert greedy_generate(next_logits, [0], 5, eos_token_id=1) == [0, 1]
    assert calls == 1


def test_zero_limit_returns_a_copy_without_calling_model() -> None:
    def unexpected_callback(prefix: list[int]) -> torch.Tensor:
        pytest.fail(f"Callback called despite a zero generation limit: {prefix}")

    prompt = [1, 2]
    result = greedy_generate(unexpected_callback, prompt, 0)
    assert result == prompt
    assert result is not prompt


def test_prompt_eos_does_not_stop_new_generation() -> None:
    result = greedy_generate(
        lambda prefix: torch.tensor([0.0, 4.0, 1.0]), [0, 2], 2, eos_token_id=2
    )
    assert result == [0, 2, 1, 1]


def test_argmax_selection_and_default_no_eos() -> None:
    result = greedy_generate(lambda prefix: torch.tensor([-8.0, -3.0, -1.0]), [0], 3)
    assert result == [0, 2, 2, 2]


def test_equal_maxima_choose_first_index() -> None:
    result = greedy_generate(lambda prefix: torch.tensor([0.0, 2.0, 2.0]), [0], 1)
    assert result == [0, 1]
