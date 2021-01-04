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

from competitive_algorithms.mathematics import extgcd


def main():
    # TMP: あってそうだが、サンプル通らない
    T = int(input())
    for i in range(T):
        N, S, K = map(int, input().split())
        m = gcd(N, K)
        N //= m
        K //= m
        right = N - S
        if right % m != 0:
            print(-1)
            continue
        right //= m

        if gcd(K, N) != 1:
            print(-1)
            continue
        x, y, _ = extgcd(K, N)
        x *= right
        y *= right
        min_x = 10 ** 10
        for i in range(-100000, 100000):
            x_i = N * i + x
            if x_i >= 0:
                min_x = min(x_i, min_x)
        print(min_x)


if __name__ == "__main__":
    main()
