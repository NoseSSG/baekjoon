# https://www.acmicpc.net/problem/16236
import sys
# sys.stdin = open('input_16236.txt','r')

from collections import deque

def find_shark():
    for i in range(N):
        for j in range(N):
            if sea[i][j] == 9:
                sea[i][j] = 0
                return (i,j)


def BFS(shark):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    visited = [[False] * N for _ in range(N)]
    d_que = deque()
    d_que.append((shark,0))
    visited[shark[0]][shark[1]] = True

    fish = []

    while d_que:
        (x,y),dist = d_que.popleft()
        for d in range(4):
            nx,ny = x+dx[d],y+dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] : continue
                if sea[nx][ny] <= size:
                    if 0 < sea[nx][ny] < size:
                        fish.append([dist+1,nx,ny])
                    d_que.append(((nx,ny),dist+1))
                visited[nx][ny] = True
    return fish

N = int(input())
sea = [list(map(int,input().split())) for _ in range(N)]
shark = find_shark()

size = 2
ans = 0
eat_fish = 0
while True:
    fishes = BFS(shark)
    if not fishes:break
    fishes.sort()
    fish = fishes[0]
    ans += fish[0]
    sea[fish[1]][fish[2]] = 0
    shark = (fish[1],fish[2])
    eat_fish +=1
    if eat_fish == size:
        size +=1
        eat_fish = 0
print(ans)