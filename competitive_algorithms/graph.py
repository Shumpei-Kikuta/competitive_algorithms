from typing import Dict, List, Tuple
import heapq

INF = 10 ** 10


class Edge:
    def __init__(self, from_: int, to_: int, d: int):
        self.from_ = from_
        self.to_ = to_
        self.d = d


class Graph:
    def __init__(self, adjacent_lists: Dict[int, Dict[int, int]]):
        # 隣接リスト
        # {1: {2: 4, 3: 5}}など
        self.adjacent_lists = adjacent_lists
        self.edges: List[Edge] = self.initialize_edgelists()
        # TODO: edge_queueの定義
        self.edge_queues = []

    def initialize_edgelists(self):
        edges = []
        for from_ in self.adjacent_lists.keys():
            for to_, d in self.adjacent_lists[from_].items():
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

    # def dijkstra(self, s):
    #     alreadys = [False] * len(self.adjacent_lists)
    #     distances = {node: INF for node in self.adjacent_lists.keys()}
    #     now = s
    #     distances[s] = 0
    #     for (to_, d) in self.adjacent_lists[now].items():
    #         heapq.heappush(self.edge_queues, (d, now, to_))
    #         distances[to_] = d
    #     alreadys[s] = True

    #     while(len(self.edge_queues) != 0):
    #         d, _, now = heapq.heappop(self.edge_queues)
    #         if alreadys[now]:
    #             continue
    #         alreadys[now] = True
    #         for next_node, d in self.adjacent_lists[now].items():
    #             # if alreadys[next_node]:
    #             #     continue
    #             distances[next_node] = min(distances[next_node], distances[now] + self.adjacent_lists[now][next_node])
    #             heapq.heappush(self.edge_queues, (d, now, next_node))
    #     return distances
    def dijkstra(self, s):
        alreadys = [False] * len(self.adjacent_lists)
        distances = {node: INF for node in self.adjacent_lists.keys()}
        now = s
        distances[s] = 0
        for (to_, d) in self.adjacent_lists[now].items():
            heapq.heappush(self.edge_queues, (d, to_))
            distances[to_] = d
        alreadys[s] = True

        while len(self.edge_queues) != 0:
            d, now = heapq.heappop(self.edge_queues)
            if alreadys[now]:
                continue
            alreadys[now] = True
            for next_node, d in self.adjacent_lists[now].items():
                if alreadys[next_node]:
                    continue
                if distances[next_node] > distances[now] + d:
                    distances[next_node] = distances[now] + d
                    heapq.heappush(self.edge_queues, (distances[next_node], next_node))
        return distances


# v, e, r = map(int, input().split())
# adjacent_lists = {node: dict() for node in range(v)}
# for _ in range(e):
#     s, t, d = map(int, input().split())
#     adjacent_lists[s][t] = d
# graph = Graph(adjacent_lists)
# result = graph.dijkstra(r)
# for v in result.values():
#     if v == 10**10:
#         print("INF")
#     else:
#         print(v)
