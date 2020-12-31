"""数学系のアルゴリズム"""
import math
from typing import Tuple


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
