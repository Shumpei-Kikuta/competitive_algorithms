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
INF = 0


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


class SegmentTree:
    # 初期化処理
    # f : SegmentTreeの演算子(区間ごとの最小を持つならmin)
    # default : fに対する単位元
    def __init__(self, size, f=lambda x, y: x + y, default=0):
        self.size = 2 ** (size - 1).bit_length()  # 簡単のため要素数Nを2冪にする
        self.default = default
        self.dat = [default] * (self.size * 2 - 1)  # 要素を単位元で初期化
        self.f = f

    def build(self, init_lists: List[int]):
        """
        初期化用のメソッド
        """
        N = len(init_lists)
        for i in range(N):
            self.update(i, init_lists[i])

    def update(self, i, x):
        i += self.size - 1
        self.dat[i] = x
        while i > 0:
            i = (i - 1) >> 1
            self.dat[i] = self.f(self.dat[i * 2 + 1], self.dat[i * 2 + 2])

    def query(self, l, r, k=0, L=0, R=None):
        """
        [l, r)における区間の演算をする
        NOTE: 右側は開区間であることに注意
        """
        if R is None:
            R = self.size
        if R <= l or r <= L:
            return self.default
        if l <= L and R <= r:
            return self.dat[k]
        else:
            lres = self.query(l, r, k * 2 + 1, L, (L + R) >> 1)
            rres = self.query(l, r, k * 2 + 2, (L + R) >> 1, R)
            return self.f(lres, rres)


def main():
    N, Q = read_int_n()
    A = read_int_n()
    segtree = SegmentTree(default=0, size=N, f=lambda x, y: x ^ y)
    segtree.build(A)

    for i in range(Q):
        t, x, y = read_int_n()
        if t == 1:
            # 置換
            segtree.update(x - 1, A[x - 1] ^ y)
            A[x - 1] = A[x - 1] ^ y
        else:
            print(segtree.query(x - 1, y))


if __name__ == "__main__":
    main()
