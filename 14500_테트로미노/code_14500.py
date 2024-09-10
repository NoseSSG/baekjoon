# https://www.acmicpc.net/problem/14500
import sys
sys.stdin = open('input_14500.txt','r')

from collections import deque

def BFS(x,y):
    global ans
    d_que = deque()
    temp_set = set()
    temp_set.add((x,y))
    d_que.append(temp_set)

    while d_que:
        temp = d_que.popleft()
        if len(temp) == 4:
            cnt = 0
            for i,j in temp:
                cnt += num[i][j]
            ans = max(ans,cnt)
            continue

        for now_x,now_y in temp:
            for d in range(4):
                nx,ny = now_x+dx[d], now_y+dy[d]
                if 0<= nx < N and 0<= ny <M:
                    if (nx,ny) not in temp and (nx,ny) not in visited:
                        t = temp.copy()
                        t.add((nx,ny))
                        d_que.append(t)



N,M = map(int,input().split())
num = [list(map(int,input().split())) for _ in range(N)]
visited = set()
dx = [1,0,-1,0]
dy = [0,1,0,-1]
ans = 0
for i in range(N):
    for j in range(M):
        BFS(i,j)
        visited.add((i,j))
print(ans)