import sys
from typing import List, Set, Dict, Tuple

sys.setrecursionlimit(10000000)
import numpy as np
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
    N, M = read_int_n()
    B = np.zeros((N, M))
    for i in range(N):
        lists = input()
        for j in range(M):
            B[i][j] = int(lists[j])
    A = np.zeros((N, M))
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            A[i][j] = B[i - 1][j]
        for j in range(1, M - 1):
            B[i][j] = B[i][j] - A[i][j - 1] - A[i][j + 1] - A[i - 1][j]

    for i in range(N):
        for j in range(M):
            print(int(A[i][j]), end="")
        print()


if __name__ == "__main__":
    main()
