from glob import glob
import pathlib

import pytest

from competitive_algorithms.graph import Graph

TEST_INPUTS = pathlib.Path("tests/inputs")
NEGATIVE_CYCLE = "NEGATIVE CYCLE"


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


@pytest.mark.parametrize(
    "input_path, start, goal, expected",
    [
        pytest.param(
            TEST_INPUTS / "warshall_floyd" / "sample01.txt", 0, 3, 4, id="sample1-1"
        ),
        pytest.param(
            TEST_INPUTS / "warshall_floyd" / "sample01.txt", 3, 0, "INF", id="sample1-2"
        ),
        pytest.param(
            TEST_INPUTS / "warshall_floyd" / "sample02.txt",
            0,
            1,
            NEGATIVE_CYCLE,
            id="sample1-2",
        ),
    ],
)
def test_warshall_floyd(input_path, start, goal, expected):
    with open(input_path, "r") as f:
        V, E = map(int, f.readline().split())
        adjacent_lists = {i: dict() for i in range(V)}
        for _ in range(E):
            s, t, w = map(int, f.readline().split())
            adjacent_lists[s][t] = w
    graph = Graph(adjacent_lists)
    actual = graph.warshall_floyd()
    if expected == NEGATIVE_CYCLE:
        assert actual == NEGATIVE_CYCLE
    elif actual[start][goal] > 10 ** 8:
        actual[start][goal] = "INF"
        assert actual[start][goal] == expected
    else:
        assert actual[start][goal] == expected
