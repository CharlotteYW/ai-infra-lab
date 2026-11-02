"""Learner-owned P1.W1 generation exercise; intentionally unimplemented."""

from collections.abc import Callable

from torch import Tensor

NextTokenLogits = Callable[[list[int]], Tensor]


def greedy_generate(
    next_token_logits: NextTokenLogits,
    prompt_ids: list[int],
    max_new_tokens: int,
    *,
    eos_token_id: int | None = None,
) -> list[int]:
    """Return a new prompt-plus-generation list using highest-scoring token IDs.

    Inputs are valid: nonempty prompt, nonnegative limit, and a callback returning
    finite 1-D CPU logits for the full current prefix. Ties use the first index.
    Do not mutate prompt_ids. Include a generated EOS and stop immediately after
    it; EOS already in the prompt does not stop generation. A zero limit calls
    no callback and returns a copy of the prompt. No model or cache is required.
    """
    raise NotImplementedError("P1.W1 Exercise B: implement bounded greedy generation.")
