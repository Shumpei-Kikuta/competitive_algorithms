from typing import List


class UnionFindTree:
    # verified by atc001
    """
    UnionFindTree
    併合、same判定ともに計算量O(α(n))
    α: アッカーマン関数でlog(n)より小さい
    縮約により全てのノードがrootとつながっているため検索が容易
    """

    def __init__(self, n: int):
        self.__n = n
        self.__parents = [None for i in range(self.__n)]
        self.__ranks = [0 for i in range(self.__n)]

    def is_same(self, x: int, y: int):
        if self.root(x) == self.root(y):
            return True
        else:
            return False

    def union(self, x: int, y: int):
        if self.is_same(x, y):
            return
        # 辺の縮約: 全ての子の親をrootにする
        if self.__ranks[x] <= self.__ranks[y]:
            self.__parents[x] = self.root(y)
            self.__ranks[x] = 1
        else:
            self.__parents[y] = self.root(x)
            self.__ranks[y] = self.__ranks[x] + 1

    def root(self, x: int):
        """
        xのrootを返す
        """
        if self.__parents[x] is None:
            return x
        else:
            self.__parents[x] = self.root(self.__parents[x])
            return self.__parents[x]


class SegmentTree:
    # verified by abc185-f
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
