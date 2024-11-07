# https://www.acmicpc.net/problem/2638
import sys
sys.stdin = open('input_2638.txt','r')

from collections import deque

def BFS_AIR():
    d_que = deque()
    d_que.append((0,0))
    visited = [[False] * M for _ in range(N)]
    count_air = [[0] * M for _ in range(N)]
    while d_que:
        x,y = d_que.popleft()
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if plate[nx][ny] == 1:
                    count_air[nx][ny] += 1
                else:
                    if not visited[nx][ny]:
                        d_que.append((nx,ny))
                visited[nx][ny] = True
    melt_count = 0
    for i in range(N):
        for j in range(M):
            if count_air[i][j] >= 2:
                melt_count+=1
                plate[i][j] = 0
    return melt_count


N,M = map(int,input().split())
plate = [list(map(int,input().split())) for _ in range(N)]
ans = 0
count = sum(sum(i) for i in plate)

while count:
    ans += 1
    count -= BFS_AIR()
print(ans)