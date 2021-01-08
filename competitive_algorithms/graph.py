from typing import Dict, List, Tuple
import heapq
from heapq import heappush, heappop

INF = 10 ** 20


class Edge:
    def __init__(self, from_: int, to_: int, d: int):
        self.from_ = from_
        self.to_ = to_
        self.d = d


class Graph:
    def __init__(self, adjacent_lists: Dict[int, Dict[int, int]]):
        # 隣接リスト
        # {1: {2: 4, 3: 5}}など
        if len(adjacent_lists) < 1:
            raise ValueError("graph size must be more than 1!")
        self.adjacent_lists = adjacent_lists

    @staticmethod
    def initialize_edgelists(adjacent_lists):
        edges = []
        for from_ in adjacent_lists.keys():
            for to_, d in adjacent_lists[from_].items():
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
        self.edges: List[Edge] = self.initialize_edgelists(self.adjacent_lists)

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

    def dijkstra(self, s):

        queue = []
        alreadys = [False] * len(self.adjacent_lists)
        distances = {node: INF for node in self.adjacent_lists.keys()}
        now = s
        distances[s] = 0
        for (to_, d) in self.adjacent_lists[now].items():
            heapq.heappush(queue, (d, to_))
            distances[to_] = d
        alreadys[s] = True

        while len(queue) != 0:
            d, now = heapq.heappop(queue)
            if alreadys[now]:
                continue
            alreadys[now] = True
            for next_node, d in self.adjacent_lists[now].items():
                if alreadys[next_node]:
                    continue
                if distances[next_node] > distances[now] + d:
                    distances[next_node] = distances[now] + d
                    heapq.heappush(queue, (distances[next_node], next_node))
        return distances

    def warshall_floyd(self):
        node2ids = {node: idx for idx, node in enumerate(self.adjacent_lists)}
        N = len(node2ids)

        # dp[i][j] = 元のコスト
        # dp[i][i] = 0で初期化
        dp = []
        for i in range(N):
            lists = []
            for j in range(N):
                lists.append(INF)
            dp.append(lists)

        for i in range(N):
            dp[i][i] = 0

        for from_ in self.adjacent_lists:
            for to_, d in self.adjacent_lists[from_].items():
                from_ = node2ids[from_]
                to_ = node2ids[to_]
                dp[from_][to_] = d

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        for i in range(N):
            if dp[i][i] < 0:
                return "NEGATIVE CYCLE"
        return dp

    def prim(self):
        # verified by aoj minimum spanning tree
        """最小全域木の辺の総和を求めるアルゴリズム
        計算量 O(|E|log(|V|))
        Note:
            最小全域木は無向グラフであるため、隣接リストの初期化に注意
        Returns:
            [type]: [description]
        """
        alreadys = [False] * len(self.adjacent_lists)
        queue = []
        min_cost = 0

        alreadys[0] = True
        for to, d in self.adjacent_lists[0].items():
            heappush(queue, (d, to))
        while len(queue) != 0:
            d, from_ = heappop(queue)
            if alreadys[from_] is True:
                continue
            alreadys[from_] = True
            min_cost += d
            for to_, d in self.adjacent_lists[from_].items():
                if alreadys[to_] is True:
                    continue
                heappush(queue, (d, to_))
        return min_cost
