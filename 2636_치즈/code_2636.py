# https://www.acmicpc.net/problem/2636
import sys
sys.stdin = open('input_2636.txt')

from collections import deque

def BFS():
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    visited = [[False]*M for _ in range(N)]
    visited[0][0] = True
    d_que = deque()
    d_que.append((0,0))
    melt_cheese = []
    while d_que:
        x,y = d_que.popleft()
        for d in range(4):
            nx,ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    if cheese[nx][ny] == 1:
                        melt_cheese.append((nx,ny))
                    else:
                        d_que.append((nx,ny))
    for x,y in melt_cheese:
        cheese[x][y] = 0
    return len(melt_cheese)


N,M = map(int,input().split())
cheese = [list(map(int,input().split())) for _ in range(N)]
ans = 0
time = 0
for i in cheese:
    ans += sum(i)
while True:
    time +=1
    temp = BFS()
    if ans == temp:
        break
    ans -= temp
print(time)
print(ans)
