# https://www.acmicpc.net/problem/2252
import sys
# sys.stdin = open('input_2252.txt','r')

from collections import deque

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
edge = [0] *(N+1)
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    edge[b] += 1
d_que = deque()
for idx in range(1,N+1):
    if edge[idx] == 0:
        d_que.append(idx)
ans = []
while d_que:
    now = d_que.popleft()
    ans.append(now)
    for next in graph[now]:
        edge[next] -= 1
        if edge[next] == 0:
            d_que.append(next)
print(*ans)
