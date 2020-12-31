"""数学系のアルゴリズム"""
import math
from typing import Tuple, List, Dict
from collections import defaultdict


def extgcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    ax + by = gcd(a,b) = d となる (x,y,d) を返す
    """
    if b == 0:
        return (1, 0, a)
    q, r = a // b, a % b
    x, y, d = extgcd(b, r)
    s, t = y, x - q * y
    return s, t, d


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


def list_prime_factor(n: int) -> Dict[int, int]:
    # TODO: verify
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
        while(i * i <= n):
            while (n % i == 0):
                n = n // i
                factors[i] += 1
            i += 1
        if n != 1:
            factors[n] += 1
        return factors
