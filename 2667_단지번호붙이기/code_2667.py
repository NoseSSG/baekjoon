# https://www.acmicpc.net/problem/2667
import sys
sys.stdin = open('input_2667.txt')

from collections import deque

def BFS(i,j):
    d_que = deque()
    temp[i][j] = 0
    d_que.append((i,j))
    ans = 1
    while d_que:
        x,y = d_que.popleft()
        for d in range(4):
            nx,ny = x + dx[d], y + dy[d]
            if 0<= nx < N and 0 <= ny < N and temp[nx][ny]==1:
                temp[nx][ny] = 0
                d_que.append((nx,ny))
                ans += 1
    return ans



N = int(input())
temp = [list(map(int,input())) for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
ans = []
for i in range(N):
    for j in range(N):
        if temp[i][j] == 1:
            ans.append(BFS(i,j))
print(len(ans))
ans.sort()
for i in ans:
    print(i)