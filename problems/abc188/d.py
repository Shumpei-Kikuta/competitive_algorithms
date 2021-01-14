import sys
from typing import List, Set, Dict, Tuple

sys.setrecursionlimit(10000000)
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

MAX_A = float("inf")


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def compress_1dim(lists: List[int]) -> Dict[int, int]:
    lists_sort = sorted(list(set(lists)))
    dicts = {}
    for value in lists:
        idx = bisect_left(lists_sort, value)
        dicts[value] = idx
    return dicts


def main():
    N, Cost = read_int_n()
    A = []
    B = []
    C = []
    days = []
    for i in range(N):
        a, b, c = read_int_n()
        A.append(a)
        B.append(b)
        C.append(c)
        days.append(a)
        days.append(b)
        days.append(b + 1)
    days_dicts = compress_1dim(days)
    days_dicts_inv = {v: k for k, v in days_dicts.items()}

    imos_sums = [0] * (len(days_dicts) + 1)
    for i, a in enumerate(A):
        imos_sums[days_dicts[a]] += C[i]
    for i, b in enumerate(B):
        imos_sums[days_dicts[b] + 1] -= C[i]
    acc_sums = list(accumulate(imos_sums))

    ans = 0
    days_dicts_inv[len(days_dicts_inv)] = days_dicts_inv[len(days_dicts_inv) - 1] + 1

    for i, sum_ in enumerate(acc_sums):
        if i == len(acc_sums) - 1:
            continue
        if sum_ > Cost:
            ans += Cost * (days_dicts_inv[i + 1] - days_dicts_inv[i])
        else:
            ans += sum_ * (days_dicts_inv[i + 1] - days_dicts_inv[i])
    print(ans)


if __name__ == "__main__":
    main()
