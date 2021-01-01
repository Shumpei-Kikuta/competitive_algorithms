import sys
sys.setrecursionlimit(10000000)
from heapq import heapify, heappop, heappush
import copy
from math import gcd, ceil
from collections import deque, defaultdict
from typing import Set
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
from itertools import permutations,combinations  # 順列、組み合わせ
# for i in combinations(A,2):
#     print(i, end=' ')
# (1, 2) (1, 3) (1, 4) (2, 3) (2, 4) (3, 4)
# pow(n,m,p): 繰り返し二乗法での計算
# from dataclasses import dataclass
def list_divisors(n: int) -> Set[int]:
    # TODO: verify
    """
    nの約数のリストを返す
    """
    i = 1
    divisors = set()

    if is_prime(n):
        divisors.add(1)
        divisors.add(n)
        return divisors

    while(i * i <= n):
        if n % i == 0:
            divisors.add(i)
            if n // i != i:
                divisors.add(n // i)
        i += 1
    return divisors


def is_prime(n: int) -> bool:
    """
    素数か判定するO(√n)
    NOTE:
        simpyライブラリはatcoderでは使えない
    """
    if n < 2:
        return False

    i = 2
    while(i * i <= n):
        if n % i == 0:
            return False
        i += 1
    return True


def main(A, B):
    a_divisors = list_divisors(A)
    b_divisors = list_divisors(B)

    divisors = a_divisors & b_divisors
    
    dicts = {d: True for d in sorted(divisors)}
    num = 0
    for i in sorted(divisors):
        if dicts[i] is False:
            continue

        if i == 1:
            num += 1
            continue
        dicts[i] = False
        num += 1
        for k, v in dicts.items():
            if k % i == 0:
                dicts[k] = False
    return num


if __name__ == '__main__':
    A, B = map(int, input().split())
    print(main(A, B))
