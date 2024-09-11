# https://www.acmicpc.net/problem/1916
import heapq
import sys
# sys.stdin = open('input_1916.txt','r')

import heapq


def dijkstra(s):
    # visited[s] = True
    # table[s][s] = 0
    h_que = []
    heapq.heappush(h_que,(0,s))
    while h_que:
        cost,now = heapq.heappop(h_que)
        if visited[now]: continue
        visited[now] = True
        ans[now] = cost
        if now == end:
            return
        for idx in range(N+1):
            if table[now][idx] == float('inf'): continue
            if visited[idx]: continue
            heapq.heappush(h_que,(cost+table[now][idx],idx))


N = int(input())
M = int(input())
table = [[float('inf')]*(N+1) for _ in range(N+1)]
visited = [False] * (N+1)
ans = [float('inf')] * (N+1)
for _ in range(M):
    a,b,c = map(int,input().split())
    table[a][b] = min(table[a][b],c)
start,end = map(int,input().split())
dijkstra(start)
print(ans[end])
# print(table[start][end])


# import heapq
#
# def dijkstra(start):
#     h_que = []
#     heapq.heappush(h_que,(0,start))
#     while h_que:
#         cost,now = heapq.heappop(h_que)
#         if cost > ans[now]: continue
#         if now == end_node:
#             print(cost)
#             return
#         if now not in graph: continue
#         for edge,next_node in graph[now]:
#             if edge+cost > ans[next_node] : continue
#             heapq.heappush(h_que,(edge+cost,next_node))
#
#
# N = int(input())
# M = int(input())
# graph = {}
# ans = [float('inf')] * (N+1)
# for _ in range(M):
#     a,b,c = map(int,input().split())
#     if a not in graph:
#         graph[a] = []
#     graph[a].append([c,b])
#
# start_node, end_node = map(int,input().split())
# dijkstra(start_node)