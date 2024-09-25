# https://www.acmicpc.net/problem/11779
import sys
sys.stdin = open('input_11779.txt','r')

import heapq

def dijkstra(start):
    global route
    h_que = []
    heapq.heappush(h_que,(0,start,[start]))

    while h_que:
        dist_sum,now,now_route = heapq.heappop(h_que)
        if dist_sum > dist[now]:
            continue
        if now == end:
            print(dist_sum)
            route = now_route
        dist[now] = dist_sum
        if now not in bus_route: continue
        for next in bus_route[now]:
            next_edge = bus_route[now][next]
            if dist[next] > dist_sum + next_edge:
                heapq.heappush(h_que,(dist_sum+next_edge,next,now_route+[next]))
                dist[next] = dist_sum + next_edge



N = int(input())
M = int(input())
bus_route = {}
for _ in range(M):
    a,b,c = map(int,input().split())
    if a not in bus_route:
        bus_route[a] = {}
    if b not in bus_route[a]:
        bus_route[a][b] = c
    else:
        bus_route[a][b] = min(bus_route[a][b],c)
dist = [float('inf')] * (N+1)
route = []
start, end = map(int,input().split())
dijkstra(start)
print(len(route))
print(*route)

