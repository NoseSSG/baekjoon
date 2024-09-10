# https://www.acmicpc.net/problem/10026
import sys
sys.stdin = open('input_10026.txt','r')

from collections import deque

def normal(x,y):
    temp = deque()
    temp.append((x,y))
    color = picture[x][y]
    while temp:
        now_x,now_y = temp.popleft()
        if visited[now_x][now_y] == 1: continue
        visited[now_x][now_y] = 1
        for d in range(4):
            nx,ny = now_x+dx[d],now_y+dy[d]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny]==0 and picture[nx][ny]==color:
                temp.append((nx,ny))

def blind(x,y):
    temp = deque()
    temp.append((x, y))
    color = picture[x][y]
    if color == 'B':
        while temp:
            now_x, now_y = temp.popleft()
            if visited2[now_x][now_y] == 1: continue
            visited2[now_x][now_y] = 1
            for d in range(4):
                nx, ny = now_x + dx[d], now_y + dy[d]
                if 0 <= nx < N and 0 <= ny < N and visited2[nx][ny] == 0 and picture[nx][ny] == color:
                    temp.append((nx, ny))
    else:
        while temp:
            now_x, now_y = temp.popleft()
            if visited2[now_x][now_y] == 1: continue
            visited2[now_x][now_y] = 1
            for d in range(4):
                nx, ny = now_x + dx[d], now_y + dy[d]
                if 0 <= nx < N and 0 <= ny < N and visited2[nx][ny] == 0 and (picture[nx][ny] == 'R' or picture[nx][ny] == 'G') :
                    temp.append((nx, ny))

N = int(input())
picture = [list(map(str,input().rstrip())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
visited2 = [[0]*N for _ in range(N)]
normal_ = 0
red_green = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            normal(i,j)
            normal_ += 1
        if visited2[i][j] == 0:
            blind(i,j)
            red_green += 1
print(normal_,red_green)