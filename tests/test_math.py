import pytest

from competitive_algorithms.mathematics import (
    extgcd,
    is_prime,
    list_prime_factor,
    list_divisors,
    lcm,
    eratosthenes,
    compress_1dim,
)


@pytest.mark.parametrize(
    "a,b", {pytest.param(4, 11, id="あり本サンプル"),},
)
def test_extgcd(a, b):
    assert extgcd(a, b) == (3, -1, 1)


@pytest.mark.parametrize(
    "n, result",
    {
        pytest.param(18, False, id="simple1"),
        pytest.param(81, False, id="simple2"),
        pytest.param(17, True, id="simple3"),
        pytest.param(1, False, id="corner1"),
        pytest.param(2, True, id="corner2"),
    },
)
def test_is_prime(n, result):
    assert is_prime(n) == result


@pytest.mark.parametrize(
    "n, result",
    [
        pytest.param(18, {2: 1, 3: 2}, id="simple"),
        pytest.param(21, {3: 1, 7: 1}, id="simple2"),
        pytest.param(5, {5: 1}, id="prime"),
        pytest.param(1, {1: 1}, id="corner"),
        pytest.param(2, {2: 1}, id="corner2"),
    ],
)
def test_list_prime_factor(n, result):
    if n == 1:
        with pytest.raises(ValueError):
            list_prime_factor(n)
    else:
        assert list_prime_factor(n) == result


@pytest.mark.parametrize(
    "n, expected",
    [
        pytest.param(10, set([1, 2, 5, 10]), id="simple"),
        pytest.param(25, set([1, 5, 25]), id="simple2"),
        pytest.param(7, set([1, 7]), id="prime"),
        pytest.param(1, set([1]), id="corner"),
        pytest.param(2, set([1, 2]), id="corner"),
    ],
)
def test_list_divisors(n, expected):
    assert list_divisors(n) == expected


@pytest.mark.parametrize(
    "A, B, expected",
    [
        pytest.param(12, 18, 36),
        pytest.param(12, 11, 12 * 11),
        pytest.param(1, 1, 1),
        pytest.param(1, 2, 2),
    ],
)
def test_lcm(A, B, expected):
    assert lcm(A, B) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        pytest.param(11, 4),
        pytest.param(100, 25),
        pytest.param(10000, 1229),
        pytest.param(2, 0),
        pytest.param(1, 0),
    ],
)
def test_eratosthenes(n, expected):
    assert len(eratosthenes(n)) == expected


@pytest.mark.parametrize(
    "input_, expected",
    [
        pytest.param([5, 3, 3, 1, 6, 1], [2, 1, 1, 0, 3, 0], id="normal"),
        pytest.param(list(range(5)), list(range(5)), id="simple"),
        pytest.param([100], [0], id="edge"),
    ],
)
def test_compress_1dim(input_, expected):
    dicts = compress_1dim(input_)
    actual = [dicts[v] for v in input_]
    assert actual == expected
