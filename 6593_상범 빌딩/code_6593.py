# https://www.acmicpc.net/problem/6593
import sys

sys.stdin = open('input_6593.txt','r')

from collections import deque


def find_start(array):
    for i in range(R):
        for j in range(C):
            if array[i][j] == 'S':
                return [i,j]
    return False

def BFS(z,x,y):
    dx=[1,0,-1,0,0,0]
    dy=[0,1,0,-1,0,0]
    dz=[0,0,0,0,-1,1]
    visited = [[[float('inf')]*C for _ in range(R)] for _ in range(L)]
    visited[z][x][y] = 0
    d_que = deque()
    d_que.append((z,x,y))
    while d_que:
        now = d_que.popleft()
        if building[now[0]][now[1]][now[2]] == 'E':
            return visited[now[0]][now[1]][now[2]]
        for d in range(6):
            nz,nx,ny = now[0]+dz[d], now[1]+dx[d],now[2]+dy[d]
            if 0<= nz < L and 0 <= nx < R and 0 <= ny < C and building[nz][nx][ny] != '#':
                if visited[nz][nx][ny] > visited[now[0]][now[1]][now[2]]+1:
                    visited[nz][nx][ny] = visited[now[0]][now[1]][now[2]]+1
                    d_que.append((nz,nx,ny))




while True:
    L,R,C = map(int,input().split())
    if (L,R,C) == (0,0,0):
        break
    building = []
    start_position = ''
    for i in range(L):
        floor = [list(map(str,input())) for _ in range(R)]
        if not start_position:
            x_y_positions = find_start(floor)
            if x_y_positions:
                start_position = (i,*x_y_positions)
        input().split()
        building.append(floor)
    ans = BFS(*start_position)
    if ans == None:
        print('Trapped!')
    else:
        print(f'Escaped in {ans} minute(s).')