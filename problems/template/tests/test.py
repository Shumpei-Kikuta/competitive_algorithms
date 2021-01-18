import os

import pytest

RANGE_ = 5


@pytest.fixture()
def get_file(pytestconfig):
    return pytestconfig.getoption("file")


@pytest.fixture(autouse=True, scope="session")
def delete_file():
    yield
    for i in range(1, 6):
        os.remove(f"actual-{i}.txt")


@pytest.mark.parametrize(
    "idx",
    # TODO: argsで1-5
    list(range(1, 1 + RANGE_))
    # 1, 2, 3, 4, 5
)
def test_main(idx, get_file):
    # TODO: argsでscriptの指定
    # script = get_file
    script = get_file
    input_ = f"answer-{idx}.txt"
    expected = f"expected-{idx}.txt"
    actual = f"actual-{idx}.txt"
    command = f"poetry run python ../{script} < {input_} > {actual}"
    os.system(command)

    # actualとexpectedが同じか判定
    with open(actual) as f:
        actual = f.read()
    with open(expected) as f:
        expected = f.read()

    assert actual == expected
