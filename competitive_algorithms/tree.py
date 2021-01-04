# verified by atc001


class UnionFindTree:
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
