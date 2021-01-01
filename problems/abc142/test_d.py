import pytest


from d import main


@pytest.mark.parametrize(
    "A, B, expected",
    [
        pytest.param(12, 18, 3),
        pytest.param(420, 660, 4),
        pytest.param(1, 2019, 1),
        pytest.param(1, 1, 1),
    ],
)
def test_main(A, B, expected):
    assert main(A, B) == expected
