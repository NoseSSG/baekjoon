# https://www.acmicpc.net/problem/11403
import sys
# sys.stdin = open('input_11403.txt','r')

from collections import deque

def BFS(start):
    visited = [0]* N
    temp = deque()
    temp.append(start)
    while temp:
        now = temp.popleft()
        for idx in range(N):
            if edge[now][idx] == 1 and visited[idx] == 0:
                visited[idx] = 1
                temp.append(idx)
    ans.append(visited)

N = int(input())
edge = [list(map(int,input().split())) for _ in range(N)]
ans = []
for i in range(N):
    BFS(i)
for ii in ans:
    print(*ii)