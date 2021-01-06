from typing import Dict, List, Tuple
from collections import defaultdict

INF = 10 ** 10


class Edge:
    def __init__(self, from_: int, to_: int, d: int):
        self.from_ = from_
        self.to_ = to_
        self.d = d


class Graph:
    def __init__(self, adjacent_lists: Dict[int, List[Tuple[int, int]]]):
        self.adjacent_lists = defaultdict(int, adjacent_lists)
        self.edges: List[Edge] = self.initialize_edgelists()

    def initialize_edgelists(self):
        edges = []
        for from_ in self.adjacent_lists.keys():
            for to_, d in self.adjacent_lists[from_]:
                edge = Edge(from_, to_, d)
                edges.append(edge)
        return edges

    def bellman_ford(self, start=int) -> Dict[int, int]:
        # Verified by AOJ: Single Source Shortest Path (Negative Edges)
        """
        最短経路アルゴリズム
        負の辺や負の閉路があっても問題なし
        計算量：O(VE)
        """
        distances = {node: INF for node in self.adjacent_lists.keys()}
        distances[start] = 0
        for _ in range(len(self.adjacent_lists)):
            is_update = False
            for edge in self.edges:
                if distances[edge.from_] == INF:
                    continue
                if distances[edge.to_] > distances[edge.from_] + edge.d:
                    distances[edge.to_] = distances[edge.from_] + edge.d
                    is_update = True
            if not is_update:
                break
        else:
            return "NEGATIVE CYCLE"
        return distances
