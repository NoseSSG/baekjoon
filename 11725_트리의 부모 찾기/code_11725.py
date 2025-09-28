# https://www.acmicpc.net/problem/11725
import sys
sys.stdin = open('input_11725.txt')
from collections import deque

def bfs(start):
    que = deque()
    que.append(start)
    parent[start] = 1
    while que:
        now = que.popleft()
        for child in graph[now]:
            if parent[child]==-1:
                parent[child] = now
                que.append(child)



N = int(input())

graph = [[] for _ in range(N+1)]
parent = [-1] *(N+1)

for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
for i in range(2,N+1):
    print(parent[i])