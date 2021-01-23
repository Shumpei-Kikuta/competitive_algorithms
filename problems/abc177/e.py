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
input = sys.stdin.readline
INF = float("inf")


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def main():
    N = read_int()
    A = read_int_n()

    if max(A) == 1:
        print("pairwise coprime")
        sys.exit()

    least_factors = [INF] * (max(A) + 1)
    least_factors[1] = 1
    for i in range(2, max(A) + 1):
        if least_factors[i] == INF:
            least_factors[i] = i
            j = 2
            while i * j <= max(A):
                least_factors[i * j] = i
                j += 1

    counter = defaultdict(int)
    for i in range(N):
        each_sets = set()
        while A[i] > 1:
            divisor = least_factors[A[i]]
            each_sets.add(divisor)
            A[i] = A[i] // divisor
        for v in each_sets:
            counter[v] += 1

    max_C = max(counter.values())
    if max_C >= N:
        print("not coprime")
    elif max_C >= 2:
        print("setwise coprime")
    else:
        print("pairwise coprime")


if __name__ == "__main__":
    main()
