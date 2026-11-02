"""Learner-owned P1.W1 attention exercise; intentionally unimplemented."""

from torch import Tensor


def scaled_dot_product_attention(
    q: Tensor,
    k: Tensor,
    v: Tensor,
    *,
    causal: bool = False,
) -> Tensor:
    """Return self-attention for equal-shape CPU float32 [B, H, T, D] inputs.

    Dimensions are positive. Return the same shape; preserve gradients and inputs.
    Causal mode permits the current position and earlier positions only.
    Use tensor primitives, not a complete attention layer or framework SDPA.
    Padding, dropout, caching, and unsupported-input validation are out of scope.
    See curriculum/phase-01-foundations/week-01.md for the learning contract.
    """
    raise NotImplementedError("P1.W1 Exercise A: implement attention after the diagnostic.")
