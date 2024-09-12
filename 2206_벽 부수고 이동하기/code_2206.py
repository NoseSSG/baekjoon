# https://www.acmicpc.net/problem/2206
import sys
# sys.stdin = open('input_2206.txt','r')

from collections import deque

def BFS(i,j):
    d_que = deque()
    d_que.append((i,j,0))
    while d_que:
        x,y,can = d_que.popleft()
        if x == N-1 and y == M -1:
            return distance[can][x][y]
        for d in range(4):
            nx,ny = x+dx[d], y+dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if wall_map[nx][ny] == 1 and can == 0:
                    distance[1][nx][ny] = distance[can][x][y]+1
                    d_que.append((nx,ny,1))
                elif wall_map[nx][ny] == 0 and distance[can][nx][ny] == -1:
                    distance[can][nx][ny] = distance[can][x][y]+1
                    d_que.append((nx,ny,can))
    return distance[0][N-1][M-1]


N,M = map(int,input().split())
wall_map = [list(map(int,input().rstrip())) for _ in range(N)]
distance = [[[-1]*M for _ in range(N)] for _ in range(2)]
distance[0][0][0] = 1
dx = [1,0,-1,0]
dy = [0,1,0,-1]
print(BFS(0,0))
