# https://www.acmicpc.net/problem/15686
import sys
# sys.stdin = open('input_15686.txt','r')

from collections import deque

def DFS(cnt,idx,visited):
    global ans
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    if cnt == M:
        temp = 0
        for h in home:
            temp += visited[h[0]][h[1]]
        ans = min(ans,temp)
    if idx == len(chickens):
        return
    copy_visited = [temp[:] for temp in visited]
    d_que = deque()
    d_que.append(chickens[idx])
    copy_visited[chickens[idx][0]][chickens[idx][1]] = 0
    while d_que:
        x,y = d_que.popleft()
        for d in range(4):
            nx,ny = x+dx[d], y+dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if copy_visited[nx][ny] > copy_visited[x][y]+1:
                    copy_visited[nx][ny] = copy_visited[x][y] +1
                    d_que.append((nx,ny))
    DFS(cnt+1,idx+1,copy_visited)
    DFS(cnt,idx+1,visited)


N,M = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(N)]
ans = float('inf')
visited = [[float('inf')]*N for _ in range(N)]
chickens = []
home = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chickens.append([i,j])
        elif city[i][j] == 1:
            home.append([i,j])
DFS(0,0,visited)
print(ans)
