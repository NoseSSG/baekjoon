# https://www.acmicpc.net/problem/11437
import sys
sys.stdin = open('input_11437.txt','r')

import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 4)


def dfs(node, par, depth):
    stack = [(node, par, depth)]
    while stack:
        curr_node, curr_par, curr_depth = stack.pop()
        parent[curr_node] = curr_par
        d[curr_node] = curr_depth

        for next_node in graph[curr_node]:
            if next_node != curr_par:
                stack.append((next_node, curr_node, curr_depth + 1))


def find_parent(a, b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a


N = int(input())
graph = defaultdict(list)
parent = [0] * (N + 1)
d = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 호출
dfs(1, -1, 0)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(find_parent(a, b))


