# https://www.acmicpc.net/problem/7569
import sys
from collections import deque
sys.stdin = open('input_7569.txt','r')


def check_tamato():
    max_day = 0
    for k in range(H):
        for i in range(M):
            for j in range(N):
                if tomato[k][i][j] == 0: return -1
                max_day=max(max_day,tomato[k][i][j])
    return max_day-1

def BFS():
    while red_tomato:
        z,x,y = red_tomato.popleft()
        for d in range(6):
            nz, nx, ny =z+dz[d], x+dx[d], y+dy[d]
            if 0<= nz<H and   0 <= nx < M and 0 <= ny < N and tomato[nz][nx][ny]==0:
                red_tomato.append((nz,nx,ny))
                tomato[nz][nx][ny] = tomato[z][x][y] +1

N, M, H = map(int,input().split())
tomato = []
for _ in range(H):
    temp = [list(map(int,input().split())) for _ in range(M)]
    tomato.append(temp)

dx = [1,0,-1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,-1,1]
red_tomato = deque()
for k in range(H):
    for i in range(M):
        for j in range(N):
            if tomato[k][i][j] == 1:
                red_tomato.append((k,i,j))
BFS()
print(check_tamato())