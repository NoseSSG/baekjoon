# https://www.acmicpc.net/problem/11724
import sys
sys.stdin = open('input_11724.txt')


def DFS(node,visited):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            DFS(i,visited)

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
visited = [False] * (N+1)
for i in range(1,N+1):
    if not visited[i]:
        DFS(i,visited)
        count+=1

print(count)