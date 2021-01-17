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
    N = int(input())

    dp = [[0] * 9 for i in range(9)]

    for i in range(1, N + 1):
        length = len(str(i))
        front = int(str(i)[0])
        back = int(str(i)[-1])
        if front == 0 or back == 0:
            continue
        dp[front - 1][back - 1] += 1

    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            ans += dp[i - 1][j - 1] * dp[j - 1][i - 1]
    print(ans)


if __name__ == "__main__":
    main()
