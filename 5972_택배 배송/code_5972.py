# https://www.acmicpc.net/problem/5972
import sys
sys.stdin = open('input_5972.txt','r')

# from collections import deque
import heapq

def dijkstra(start):
    h_que = []
    heapq.heappush(h_que,(0,start))
    while h_que:
        sum_dist,now = heapq.heappop(h_que)
        if dist[now] < sum_dist: continue
        for idx,cost in graph[now]:
            sum_temp = sum_dist + cost
            if dist[idx] > sum_temp:
                dist[idx] = sum_temp
                heapq.heappush(h_que,(sum_temp, idx))


N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
dist = [float('inf')] * (N+1)
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
dijkstra(1)
print(dist[N])