# https://www.acmicpc.net/problem/1753
## 문제를 잘 읽자 inf X / INF O

import sys
sys.stdin = open('input_1753.txt')

import heapq

def dijkstra(s):
    temp = []
    heapq.heappush(temp,(0,s))
    while temp:
        dist,now = heapq.heappop(temp)
        if visited[now] != float('inf'): continue
        visited[now] = dist
        if now not in Graph: continue

        for next in Graph[now]:
            if visited[next] == float('inf'):
                heapq.heappush(temp,(dist + Graph[now][next],next))


V,E = map(int,input().split())
start = int(input())
Graph = {}
for _ in range(E):
    a,b,c = map(int,input().split())
    if a not in Graph:
        Graph[a] = {}
    if b not in Graph[a]:
        Graph[a][b] = c
    else:
        Graph[a][b] = min(Graph[a][b],c)
visited = [float('INF')] * (V+1)
dijkstra(start)
for dist in visited[1:]:
    if dist == float('inf'):
        print("INF")
    else:
        print(dist)