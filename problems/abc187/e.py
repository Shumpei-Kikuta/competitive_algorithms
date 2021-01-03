import sys
from typing import List, Set, Dict, Tuple

sys.setrecursionlimit(10000000)
# import numpy as np
from heapq import heapify, heappop, heappush
import copy
from math import gcd, ceil
from collections import deque, defaultdict

# queueとして使う場合 append(右に挿入), popleft(左を取り出す)を使う
# stackとして使う場合、append, pop(右を取り出す)
from itertools import accumulate  # 累積和の計算

# A=[1,4,3,4,6,5]
# print(list(accumulate(A))) #[1, 5, 8, 12, 18, 23]
from bisect import bisect_left, bisect_right

# bisect_left: 配列の順序関係が崩れない条件で挿入することができる一番左の点
# bisect_right: 配列の順序関係が崩れない条件で挿入することができる一番右の点
# A = [1, 1, 1, 2, 2, 2, 4]
# print(bisect_left(A, 2))  # 3
# print(bisect_right(A, 2))  # 6
# print(bisect_left(A, 3))  # 6
# print(bisect_right(A, 3))  # 6
from itertools import permutations, combinations  # 順列、組み合わせ

# for i in combinations(A,2):
#     print(i, end=' ')
# (1, 2) (1, 3) (1, 4) (2, 3) (2, 4) (3, 4)
# pow(n,m,p): 繰り返し二乗法での計算
# from dataclasses import dataclass


class Node:
    parent = -1
    children = []


def main():
    N = int(input())
    adj_list = {i: [] for i in range(N)}
    edges = []
    for i in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        adj_list[a].append(b)
        adj_list[b].append(a)
        edges.append((a, b))
    root = 0
    queue = deque()
    queue.append(root)
    tree = [Node() for i in range(N)]
    colors = [0] * N
    colors[root] = 1
    while len(queue) != 0:
        now = queue.popleft()
        for i in adj_list[now]:
            if colors[i] != 1:
                tree[i].parent = now
                tree[now].children.append(i)
                queue.append(i)
                colors[i] = 1
    Q = int(input())
    imos = []
    for i in range(Q):
        t, e, x = map(int, input().split())
        e -= 1
        # どっちが親か
        a, b = edges[e]
        if tree[a].parent == b:
            parent = b
            child = a
        else:
            parent = a
            child = b


if __name__ == "__main__":
    main()
