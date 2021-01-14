# import sys
# sys.setrecursionlimit(1000000000)
# # import numpy as np
# # queueとして使う場合 append(右に挿入), popleft(左を取り出す)を使う
# # stackとして使う場合、append, pop(右を取り出す)
# # A=[1,4,3,4,6,5]
# # print(list(accumulate(A))) #[1, 5, 8, 12, 18, 23]
# # bisect_left: 配列の順序関係が崩れない条件で挿入することができる一番左の点
# # bisect_right: 配列の順序関係が崩れない条件で挿入することができる一番右の点
# # A = [1, 1, 1, 2, 2, 2, 4]
# # print(bisect_left(A, 2))  # 3
# # print(bisect_right(A, 2))  # 6
# # print(bisect_left(A, 3))  # 6
# # print(bisect_right(A, 3))  # 6
# # for i in combinations(A,2):
# #     print(i, end=' ')
# # (1, 2) (1, 3) (1, 4) (2, 3) (2, 4) (3, 4)
# # pow(n,m,p): 繰り返し二乗法での計算
# # from dataclasses import dataclass
# from collections import deque
# input = sys.stdin.readline

# from collections import defaultdict

# class UnionFindTree():
#     def __init__(self, n):
#         self.n = n
#         self.parents = [-1] * n

#     def find(self, x):
#         if self.parents[x] < 0:
#             return x
#         else:
#             self.parents[x] = self.find(self.parents[x])
#             return self.parents[x]

#     def union(self, x, y):
#         x = self.find(x)
#         y = self.find(y)

#         if x == y:
#             return

#         self.parents[x] += self.parents[y]
#         self.parents[y] = x

#     def size(self, x):
#         return -self.parents[self.find(x)]

#     def same(self, x, y):
#         return self.find(x) == self.find(y)

#     def members(self, x):
#         root = self.find(x)
#         return [i for i in range(self.n) if self.find(i) == root]

#     def roots(self):
#         return [i for i, x in enumerate(self.parents) if x < 0]

#     def group_count(self):
#         return len(self.roots())

#     def all_group_members(self):
#         group_members = defaultdict(list)
#         for member in range(self.n):
#             group_members[self.find(member)].append(member)
#         return group_members

# def read_int():
#     return int(input())


# def read_int_n():
#     return list(map(int, input().split()))


# INF = 10 ** 20 + 1


# def main():
#     N, M = read_int_n()
#     A = read_int_n()
#     A.insert(0, 0)
#     adj_lists = {i + 1: list() for i in range(N)}
#     COLORS = [False] * (N + 1)
#     max_diff = - INF
#     min_costs = [INF] * (N + 1)

#     components = []

#     for i in range(M):
#         x, y = read_int_n()
#         adj_lists[x].append(y)
#     for i in range(1, N + 1):
#         now = i
#         max_diff = max(max_diff, A[now] - min_costs[now])
#         for next_node in adj_lists[now]:
#             min_costs[next_node] = min(min_costs[now], A[now], min_costs[next_node])
#     print(max_diff)


# if __name__ == "__main__":
#     main()


import sys

sys.setrecursionlimit(1000000000)
# import numpy as np
# queueとして使う場合 append(右に挿入), popleft(左を取り出す)を使う
# stackとして使う場合、append, pop(右を取り出す)
# A=[1,4,3,4,6,5]
# print(list(accumulate(A))) #[1, 5, 8, 12, 18, 23]
# bisect_left: 配列の順序関係が崩れない条件で挿入することができる一番左の点
# bisect_right: 配列の順序関係が崩れない条件で挿入することができる一番右の点
# A = [1, 1, 1, 2, 2, 2, 4]
# print(bisect_left(A, 2))  # 3
# print(bisect_right(A, 2))  # 6
# print(bisect_left(A, 3))  # 6
# print(bisect_right(A, 3))  # 6
# for i in combinations(A,2):
#     print(i, end=' ')
# (1, 2) (1, 3) (1, 4) (2, 3) (2, 4) (3, 4)
# pow(n,m,p): 繰り返し二乗法での計算
# from dataclasses import dataclass

# distutils: language=c++
# cython: language_level=3, boundscheck=False, wraparound=False, cdivision=True

from collections import deque

input = sys.stdin.readline

from collections import defaultdict


class UnionFindTree:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


INF = float("inf")


def main():
    # TODO: なぜTLE?
    # O(N + M)に見えるが
    N, M = read_int_n()
    A = read_int_n()
    A.insert(0, 0)
    adj_lists = {i + 1: list() for i in range(N)}
    COLORS = [False] * (N + 1)
    max_diff = -INF

    components = []

    for i in range(M):
        x, y = read_int_n()
        adj_lists[x].append(y)
    for i in range(1, N + 1):
        if COLORS[i] is False:
            queue = deque()
            min_cost = INF
            queue.append((i, min_cost))
            while len(queue) != 0:
                now, min_cost = queue.pop()
                COLORS[i] = True
                max_diff = max(max_diff, A[now] - min_cost)
                min_cost = min(min_cost, A[now])
                for next_node in adj_lists[now]:
                    queue.append((next_node, min_cost))
    print(max_diff)


if __name__ == "__main__":
    main()
