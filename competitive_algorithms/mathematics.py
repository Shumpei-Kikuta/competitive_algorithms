"""数学系のアルゴリズム"""
import math
from typing import Tuple, List, Dict, Set
from collections import defaultdict


def lcm(a: int, b: int) -> int:
    """
    a, bの最小公倍数を返す
    計算量: O(√min(a, b))
    """
    if a <= 0 or b <= 0:
        raise ValueError("a and b must not be 0")
    return a * b / math.gcd(a, b)


def extgcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    ax + by = gcd(a,b) = d となる (x,y,d) を返す
    計算量: O(log(max(a, b)))
    """
    if b == 0:
        return (1, 0, a)
    q, r = a // b, a % b
    x, y, d = extgcd(b, r)
    s, t = y, x - q * y
    return s, t, d


def is_prime(n: int) -> bool:
    """
    素数か判定する
    計算量: O(√n)
    NOTE: simpyライブラリはatcoderでは使えない
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
    素因数を列挙するアルゴリズム
    nの素因数は高々√nであることを利用(自身が素数でない場合)
    計算量: O(√n)
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


def list_divisors(n: int) -> Set[int]:
    """
    nの約数のリストを返す
    計算量: O(√n)
    """
    i = 1
    divisors = set()

    if is_prime(n):
        divisors.add(1)
        divisors.add(n)
        return divisors

    while i * i <= n:
        if n % i == 0:
            divisors.add(i)
            if n // i != i:
                divisors.add(n // i)
        i += 1
    return divisors


def eratosthenes(n: int) -> Set[int]:
    """
    エラトステネスの篩
    nより小さい素数を列挙する
    計算量: O(n loglogn) ほぼO(n)と考えて良い
    """
    primes = set()
    is_primes_dicts = {i: True for i in range(2, n)}
    if n == 1:
        return primes
    for i in range(2, n):
        if is_primes_dicts[i]:
            if is_prime(i):
                primes.add(i)
                idx = 2
                while i * idx <= n:
                    is_primes_dicts[i * idx] = False
                    idx += 1
    return primes
