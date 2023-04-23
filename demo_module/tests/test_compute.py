from demo_module.impl.compute import compute_init
import pytest


sizes = [
    (10, 10),
    (20, 20),
    (5, 15),
    (15, 5),
]


@pytest.mark.parametrize("m, n", sizes)
def test_dim(m, n):
    values = compute_init(m, n)
    assert values.shape == (m, n)
