import pytest

from competitive_algorithms.mathematics import extgcd, is_prime


@pytest.mark.parametrize("a,b", {
    pytest.param(4, 11, id="あり本サンプル"),
})
def test_extgcd(a, b):
    assert extgcd(a, b) == (3, -1, 1)

@pytest.mark.parametrize("n, result", {
    pytest.param(18, False, id="simple1"),
    pytest.param(81, False, id="simple2"),
    pytest.param(17, True, id="simple3"),
    pytest.param(1, False, id="corner1"),
    pytest.param(2, True, id="corner2")
})
def test_is_prime(n, result):
    assert is_prime(n) == result

