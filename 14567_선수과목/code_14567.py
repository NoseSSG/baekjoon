# https://www.acmicpc.net/problem/14567
import sys
# sys.stdin = open('input_14567.txt','r')

from collections import deque





N,M = map(int,input().split())
start = set([i for i in range(1,N+1)])
subject = [1] * (N+1)
ans = [1] * (N+1)
graph = {}
for _ in range(M):
    a,b = map(int,input().split())
    start.discard(b)
    if a not in graph:
        graph[a] = []
    graph[a].append(b)
    subject[b] += 1
    d_que = deque()
for first_subject in start:
    d_que.append((first_subject,1))

while d_que:
    now,cnt = d_que.popleft()
    if now not in graph: continue
    for next in graph[now]:
        subject[next] -= 1
        if subject[next] == 1:
            d_que.append((next,cnt+1))
            ans[next] = cnt + 1
print(*ans[1:])