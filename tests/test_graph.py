from glob import glob
import pathlib

import pytest

from competitive_algorithms.graph import Graph

TEST_INPUTS = pathlib.Path("tests/inputs")


@pytest.mark.parametrize(
    "input_path, expected",
    [
        pytest.param(TEST_INPUTS / "prim" / "sample01.txt", 5, id="sample1"),
        pytest.param(TEST_INPUTS / "prim" / "sample02.txt", 3, id="sample2"),
    ],
)
def test_minimum_spanning_tree(input_path, expected):
    with open(input_path, "r") as f:
        V, E = map(int, f.readline().split())
        adjacent_lists = {i: dict() for i in range(V)}
        for _ in range(E):
            s, t, w = map(int, f.readline().split())
            adjacent_lists[s][t] = w
            adjacent_lists[t][s] = w
    graph = Graph(adjacent_lists)
    assert graph.prim() == expected
