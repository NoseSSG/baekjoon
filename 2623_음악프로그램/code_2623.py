# https://www.acmicpc.net/problem/2623
import sys

sys.stdin = open('input_2623.txt')

from collections import deque

N,M = map(int,input().split())
called = [0] * (N+1)
graph = {}
for _ in range(M):
    PD = list(map(int,input().split()))
    for i in range(1,PD[0]):
        a = PD[i]
        b = PD[i+1]
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
        called[b] += 1
d_que = deque()
for i in range(1,N+1):
    if called[i] == 0:
        d_que.append(i)
ans = []
while d_que:
    now = d_que.popleft()
    ans.append(now)
    if now in graph:
        for next in graph[now]:
            called[next] -=1
            if called[next] == 0:
                d_que.append(next)

if len(ans) == N:
    for i in ans:
        print(i)
else:
    print(0)