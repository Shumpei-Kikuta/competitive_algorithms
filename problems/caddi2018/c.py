import sys

sys.setrecursionlimit(10000000)
from heapq import heapify, heappop, heappush
import copy
from math import gcd, ceil
from collections import deque, defaultdict
from typing import Tuple, List, Dict, Set

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
# from competitive_algorithms.mathematics import list_prime_factor


def is_prime(n: int) -> bool:
    """
    素数か判定するO(√n)
    NOTE:
        simpyライブラリはatcoderでは使えない
    """
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def list_prime_factor(n: int) -> Dict[int, int]:
    """
    素因数を列挙するアルゴリズムO(√n)
    nの素因数は高々√nであることを利用(自身が素数でない場合)
    """
    factors = defaultdict(int)
    if n == 1:
        raise ValueError("1 does not have factors!")
    if is_prime(n):
        factors[n] += 1
        return factors
    else:
        i = 2
        while i * i <= n:
            while n % i == 0:
                n = n // i
                factors[i] += 1
            i += 1
        if n != 1:
            factors[n] += 1
        return factors


def main():
    N, P = map(int, input().split())
    try:
        factors = list_prime_factor(P)
        # print(factors)
    except ValueError:
        print(1)
        sys.exit()
    ans = 1
    for k, v in factors.items():
        while v >= N:
            ans *= k
            v -= N
    print(ans)


if __name__ == "__main__":
    main()
