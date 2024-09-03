# https://www.acmicpc.net/problem/7576
import sys
# sys.stdin = open('input_7576.txt','r')

from collections import deque

def check_tamato():
    max_day = 0
    for i in range(M):
        for j in range(N):
            if temp[i][j] == 0: return -1
            max_day=max(max_day,temp[i][j])
    return max_day-1

def BFS():
    while red_tomato:
        x,y = red_tomato.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0 <= nx < M and 0 <= ny < N and temp[nx][ny]==0:
                red_tomato.append((nx,ny))
                temp[nx][ny] = temp[x][y]+1


N, M = map(int,input().split())
temp = [list(map(int,input().split())) for _ in range(M)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
red_tomato = deque()
for i in range(M):
    for j in range(N):
        if temp[i][j] == 1:
            red_tomato.append((i,j))
BFS()
# print(temp)
print(check_tamato())