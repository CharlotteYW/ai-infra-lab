"""Behavioral acceptance checks for the learner's attention implementation."""

import pytest
import torch
import torch.nn.functional as functional
from attention import scaled_dot_product_attention

pytestmark = pytest.mark.exercise


def inputs(shape: tuple[int, int, int, int]) -> tuple[torch.Tensor, ...]:
    generator = torch.Generator(device="cpu").manual_seed(2026)
    return tuple(torch.randn(shape, generator=generator, dtype=torch.float32) for _ in range(3))


@pytest.mark.parametrize("shape", [(1, 1, 1, 1), (2, 4, 8, 16), (2, 3, 5, 7)])
@pytest.mark.parametrize("causal", [False, True])
def test_shape_and_framework_agreement(shape: tuple[int, int, int, int], causal: bool) -> None:
    q, k, v = inputs(shape)
    original = [tensor.clone() for tensor in (q, k, v)]
    actual = scaled_dot_product_attention(q, k, v, causal=causal)
    expected = functional.scaled_dot_product_attention(q, k, v, dropout_p=0.0, is_causal=causal)
    assert actual.shape == shape
    assert actual.dtype == torch.float32
    assert actual.device.type == "cpu"
    torch.testing.assert_close(actual, expected, rtol=1e-4, atol=1e-5)
    for value, before in zip((q, k, v), original, strict=True):
        torch.testing.assert_close(value, before, rtol=0, atol=0)


def test_uniform_scores_have_known_noncausal_result() -> None:
    q = torch.zeros(1, 1, 3, 1)
    k = torch.zeros_like(q)
    v = torch.tensor([[[[1.0], [3.0], [8.0]]]])
    actual = scaled_dot_product_attention(q, k, v)
    torch.testing.assert_close(actual, torch.tensor([[[[4.0], [4.0], [4.0]]]]))


def test_uniform_scores_have_known_causal_result() -> None:
    q = torch.zeros(1, 1, 3, 1)
    k = torch.zeros_like(q)
    v = torch.tensor([[[[1.0], [3.0], [8.0]]]])
    actual = scaled_dot_product_attention(q, k, v, causal=True)
    torch.testing.assert_close(actual, torch.tensor([[[[1.0], [2.0], [4.0]]]]))


def test_future_data_cannot_change_earlier_causal_outputs() -> None:
    q, k, v = inputs((2, 3, 6, 5))
    original = scaled_dot_product_attention(q, k, v, causal=True)
    changed_q, changed_k, changed_v = (tensor.clone() for tensor in (q, k, v))
    changed_q[:, :, 3:, :] += 7.0
    changed_k[:, :, 3:, :] -= 11.0
    changed_v[:, :, 3:, :] += 100.0
    changed = scaled_dot_product_attention(changed_q, changed_k, changed_v, causal=True)
    torch.testing.assert_close(changed[:, :, :3, :], original[:, :, :3, :])


@pytest.mark.parametrize("causal", [False, True])
def test_single_token_returns_its_value(causal: bool) -> None:
    q, k, v = inputs((2, 3, 1, 5))
    torch.testing.assert_close(scaled_dot_product_attention(q, k, v, causal=causal), v)


@pytest.mark.parametrize("causal", [False, True])
def test_finite_gradients_match_framework(causal: bool) -> None:
    learner_inputs = tuple(tensor.requires_grad_() for tensor in inputs((2, 2, 4, 3)))
    reference_inputs = tuple(tensor.detach().clone().requires_grad_() for tensor in learner_inputs)
    actual = scaled_dot_product_attention(*learner_inputs, causal=causal)
    expected = functional.scaled_dot_product_attention(
        *reference_inputs, dropout_p=0.0, is_causal=causal
    )
    weights = torch.linspace(-1.0, 1.0, actual.numel()).reshape_as(actual)
    actual_gradients = torch.autograd.grad((actual * weights).sum(), learner_inputs)
    expected_gradients = torch.autograd.grad((expected * weights).sum(), reference_inputs)
    for actual_gradient, expected_gradient in zip(
        actual_gradients, expected_gradients, strict=True
    ):
        assert torch.isfinite(actual_gradient).all()
        torch.testing.assert_close(actual_gradient, expected_gradient, rtol=1e-4, atol=1e-5)


@pytest.mark.parametrize("causal", [False, True])
def test_large_finite_scores_remain_finite(causal: bool) -> None:
    q, k, v = inputs((1, 2, 4, 3))
    q, k = q * 100.0, k * 100.0
    actual = scaled_dot_product_attention(q, k, v, causal=causal)
    expected = functional.scaled_dot_product_attention(q, k, v, dropout_p=0.0, is_causal=causal)
    assert torch.isfinite(actual).all()
    torch.testing.assert_close(actual, expected, rtol=1e-4, atol=1e-5)
