"""Bootstrap checks, not assessments or inference benchmarks."""

import json
import platform
import sys

import pytest
import torch

pytestmark = pytest.mark.environment


def test_runtime_report() -> None:
    report = {
        "python": platform.python_version(),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "torch": torch.__version__,
        "mps_built": torch.backends.mps.is_built(),
        "mps_available": torch.backends.mps.is_available(),
    }
    print("\nEnvironment (not a benchmark): " + json.dumps(report, sort_keys=True))
    assert sys.version_info[:2] == (3, 11)


def test_cpu_tensor_execution() -> None:
    matrix = torch.tensor([[1.0, 2.0], [3.0, 4.0]], device="cpu")
    actual = matrix @ torch.tensor([[2.0], [1.0]], device="cpu")
    torch.testing.assert_close(actual, torch.tensor([[4.0], [10.0]]))


def test_cpu_autograd_execution() -> None:
    values = torch.tensor([2.0, -3.0], requires_grad=True, device="cpu")
    values.square().sum().backward()
    torch.testing.assert_close(values.grad, torch.tensor([4.0, -6.0]))


@pytest.mark.skipif(not torch.backends.mps.is_available(), reason="MPS is optional/unavailable")
def test_optional_mps_execution() -> None:
    matrix = torch.tensor([[1.0, 2.0], [3.0, 4.0]], device="mps")
    actual = matrix @ torch.tensor([[2.0], [1.0]], device="mps")
    torch.mps.synchronize()
    torch.testing.assert_close(actual.cpu(), torch.tensor([[4.0], [10.0]]))
