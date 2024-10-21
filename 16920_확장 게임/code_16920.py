# https://www.acmicpc.net/problem/16920
import sys
sys.stdin = open('input_16920.txt','r')

from collections import deque

def BFS():
    global flag
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    for idx in range(1,P+1):
        d_que = deque()
        for i in players[idx]:
            d_que.append((i,0))
        players[idx] = []
        while d_que:
            (x,y),count = d_que.popleft()
            for d in range(4):
                nx,ny = x+dx[d], y+dy[d]
                if 0<= nx < N and 0 <= ny < M and count <distance[idx]:
                    if castle[nx][ny] == '.':
                        castle[nx][ny] = idx
                        d_que.append(((nx,ny),count+1))
                        players[idx].append((nx,ny))
                        cnt[idx] += 1
                        flag = True

N,M,P = map(int,input().split())
distance =[0] +  list(map(int,input().split()))
castle = [list(map(str,input())) for _ in range(N)]
players = {}
flag = True
for i in range(1,P+1):
    players[i] = []
cnt = [0] * (P+1)

for i in range(N):
    for j in range(M):
        if castle[i][j] != '.' and castle[i][j] != '#':
            player = int(castle[i][j])
            players[player].append((i,j))
            cnt[player] += 1

while flag:
    flag  = False
    BFS()

print(*cnt[1:])