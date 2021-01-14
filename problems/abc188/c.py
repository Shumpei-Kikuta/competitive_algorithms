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


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def main():
    N = int(input())
    A = read_int_n()

    B = A[: 2 ** (N - 1)]
    C = A[2 ** (N - 1) :]
    max_b = -1
    max_b_idx = -1
    for i in range(len(B)):
        if max_b < B[i]:
            max_b = B[i]
            max_b_idx = i

    max_c = -1
    max_c_idx = len(B)
    for i in range(len(C)):
        if max_c < C[i]:
            max_c = C[i]
            max_c_idx = i + len(B)

    if max_b > max_c:
        print(max_c_idx + 1)
    else:
        print(max_b_idx + 1)


if __name__ == "__main__":
    main()
