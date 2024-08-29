# https://www.acmicpc.net/problem/1260
import sys
# sys.stdin = open('input_1260.txt','r')

import heapq
from collections import deque
T = 3

def DFS(start):
    if visited[start]:
        return
    dfs_ans.append(start)
    visited[start] = True
    for next in graph[start]:
        if visited[next]: continue
        DFS(next)


def BFS(start):
    d_que = deque()
    d_que.append(start)
    while d_que:
        now = d_que.popleft()
        if visited[now]: continue
        bfs_ans.append(now)
        visited[now] = True
        for next in graph[now]:
            if visited[next]: continue
            d_que.append(next)


# for test_case in range(1,T+1):
V,E,S = map(int,input().split())
graph ={}
visited = [False]*(V+1)
for i in range(1,V+1):
    graph[i] = [i]
dfs_ans = []
bfs_ans = []
for i in range(E):
    A,B = map(int,input().split())
    # if A not in graph:
    #     graph[A] = [A]
    # if B not  in graph:
    #     graph[B] = [B]
    heapq.heappush(graph[A],B)
    heapq.heappush(graph[B],A)
DFS(S)
print(*dfs_ans)
visited = [False] * (V + 1)
BFS(S)
print(*bfs_ans)
