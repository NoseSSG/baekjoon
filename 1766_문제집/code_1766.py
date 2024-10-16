# https://www.acmicpc.net/problem/1766
import sys
sys.stdin = open('input_1766.txt','r')

import heapq

N,M = map(int,input().split())
call_cnt = [0] * (N+1)
graph = {}

h_que = []

for i in range(M):
    a,b = map(int,input().split())
    if a not in graph:
        graph[a] =[]
    graph[a].append(b)
    call_cnt[b] += 1

for i in range(1,N+1):
    if call_cnt[i]==0:
        heapq.heappush(h_que,i)
ans = []
while h_que:
    now = heapq.heappop(h_que)
    ans.append(now)
    if now in graph:
        for next in graph[now]:
            call_cnt[next] -= 1
            if call_cnt[next] == 0:
                heapq.heappush(h_que,next)

print(*ans)