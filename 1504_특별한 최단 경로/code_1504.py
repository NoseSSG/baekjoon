# https://www.acmicpc.net/problem/1504
import sys
sys.stdin = open('input_1504.txt','r')

import heapq

def dijkstra(start):
    temp = []
    heapq.heappush(temp,(0,start))
    visited = [float('inf')] * (N + 1)
    while temp:
        dist,now = heapq.heappop(temp)
        if visited[now] != float('inf'): continue
        visited[now] = dist
        if now not in Graph:continue
        for next,edge in Graph[now]:
            if visited[next] != float('inf') : continue
            heapq.heappush(temp,(edge+dist,next))
    return  visited


N,E = map(int,input().split())
Graph = {}
for _ in range(E):
    a,b,c = map(int,input().split())
    if a not in Graph: Graph[a] = []
    if b not in Graph: Graph[b] = []
    Graph[a].append([b,c])
    Graph[b].append([a,c])
stop1,stop2 = map(int,input().split())
start_one = dijkstra(1)
start_stop1 = dijkstra(stop1)
start_stop2 = dijkstra(stop2)

route1 = start_one[stop1] + start_stop1[stop2] + start_stop2[N]
route2 = start_one[stop2] + start_stop2[stop1] + start_stop1[N]
ans = min(route1,route2)
if ans == float('inf'): ans = -1
print(ans)