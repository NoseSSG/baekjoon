# https://www.acmicpc.net/problem/17835
import sys
# sys.stdin = open('input_17835.txt','r')

import heapq

def dijkstra():
    h_que = []
    for g in goal:
        result[g] = 0
        heapq.heappush(h_que,(0,g))
    while h_que:
        cost,now = heapq.heappop(h_que)
        if cost > result[now]:
            continue
        for next_node in graph[now]:
            print(next_node)
            if result[next_node[0]] > cost + next_node[1]:
                result[next_node[0]] = cost + next_node[1]
                heapq.heappush(h_que,(cost + next_node[1],next_node[0]))

N,M,K = map(int,input().split())
ans = 0
ans_idx = 1
graph = [[] for _ in range(N+1)]
result =[float('inf')] * (N+1)
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[b].append([a,c])
goal = list(map(int,input().split()))
dijkstra()
for i in range(1,N+1):
    if result[i] > ans:
        ans = result[i]
        ans_idx = i
print(result)
print(ans_idx)
print(ans)