import sys
sys.stdin = open('input_1520.txt','r')

def DFS(x,y):
    global ans
    if x == N-1 and y == M-1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y] = 0
    for d in range(4):
        now = groud[x][y]
        nx, ny = x+dx[d], y+dy[d]
        if 0<= nx < N and 0<= ny < M and now > groud[nx][ny]:
            visited[x][y] += DFS(nx,ny)
    return visited[x][y]


N,M = map(int,input().split())
groud = [list(map(int,input().split())) for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
visited = [[-1] * M for _ in range(N)]

ans = 0

print(DFS(0,0))
