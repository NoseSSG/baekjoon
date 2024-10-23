# https://www.acmicpc.net/problem/2637
import sys
sys.stdin = open('input_2637.txt','r')

from collections import deque

N = int(input())
degrees = [0] *(N+1)
graph = [[]*(N+1) for _ in range(N+1)]
count = [[0]*(N+1) for _ in range(N+1)]
M = int(input())
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[b].append([a,c])
    degrees[a] += 1
d_que = deque()
for i in range(1,N+1):
    if degrees[i] == 0:
        d_que.append(i)
while d_que:
    now = d_que.popleft()
    for next_node in graph[now]:
        if sum(count[now]) == 0:
            count[next_node[0]][now] = next_node[1]
        else:
            for i in range(1,N+1):
                count[next_node[0]][i] += (count[now][i] * next_node[1])
        degrees[next_node[0]] -= 1
        if degrees[next_node[0]] == 0:
            d_que.append(next_node[0])
for idx,val in enumerate(count[N]):
    if val != 0 :
        print(idx,val)