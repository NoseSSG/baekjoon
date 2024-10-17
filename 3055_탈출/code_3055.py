# https://www.acmicpc.net/problem/3055
import sys
# sys.stdin = open('input_3055.txt','r')

from collections import deque

def bfs(temp):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while temp:
        x,y= temp.popleft()
        if (x,y) == goal:
            return distance[x][y]
        for d in range(4):
            nx,ny = x + dx[d], y + dy[d]
            if 0 <= nx < R and 0 <= ny < C:
                if (map[nx][ny]=='.' or map[nx][ny]=='D') and map[x][y] =='S':
                    map[nx][ny] = 'S'
                    distance[nx][ny] = distance[x][y]+1
                    temp.append((nx,ny))
                if (map[nx][ny]=='.' or map[nx][ny]=='S') and map[x][y] == '*':
                    map[nx][ny] = '*'
                    temp.append((nx,ny))

    return "KAKTUS"


R,C = map(int,input().split())
map = [list(input()) for _ in range(R)]
distance = [[0]*C for _ in range(R)]

d_que = deque()

hedgehog = []
water = []
for i in range(R):
    for j in range(C):
        if map[i][j] == 'S':
            hedgehog.append((i,j))
        elif map[i][j] == '*':
            water.append((i,j))
        elif map[i][j] == 'D':
            goal = (i,j)

d_que.append(hedgehog[0])
for w in water:
    d_que.append(w)
print(bfs(d_que))