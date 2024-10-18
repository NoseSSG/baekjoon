# https://www.acmicpc.net/problem/17836
import sys
sys.stdin = open('input_17836.txt','r')

from collections import deque

def BFS():
    d_que = deque()
    d_que.append((0,0,False))
    time[0][0] = 0
    sword_idx = []
    while d_que:
        x,y,sword = d_que.popleft()
        if (x,y) == (N-1,M-1):
            break
        for d in range(4):
            nx,ny = x+dx[d],y+dy[d]
            if 0 <= nx < N and 0 <= ny < M and time[nx][ny] > time[x][y]+1:
                if castle[nx][ny] != 1:
                    if castle[nx][ny] == 2:
                        sword_idx = [nx,ny]
                    else:
                        d_que.append((nx,ny,sword))
                    time[nx][ny] = time[x][y] + 1
    if sword_idx:
        return min(time[N-1][M-1],time[sword_idx[0]][sword_idx[1]]+(abs(sword_idx[0]-(N-1)) + abs(sword_idx[1] -(M-1)) ))
    else:
        return time[N-1][M-1]


N,M,T = map(int,input().split())

castle = [list(map(int,input().split())) for _ in range(N)]
time = [[float('inf')]*M for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
ans = BFS()
if ans > T:
    print("Fail")
else:
    print(ans)
