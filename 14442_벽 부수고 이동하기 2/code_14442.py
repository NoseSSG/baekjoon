# https://www.acmicpc.net/problem/14442
import sys
# sys.stdin = open('input_14442.txt','r')

from collections import deque

def BFS():
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    d_que = deque()
    d_que.append((0,0,0))
    visited[0][0][0] = 1
    while d_que:
        x,y,cnt = d_que.popleft()
        if (x,y) == (N-1,M-1):
            return visited[cnt][x][y]
        for d in range(4):
            nx,ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if map[nx][ny] == 0 and visited[cnt][nx][ny] > visited[cnt][x][y] + 1:
                    visited[cnt][nx][ny] = visited[cnt][x][y] + 1
                    d_que.append((nx,ny,cnt))
                if map[nx][ny] == 1 and cnt < K:
                    if visited[cnt+1][nx][ny] > visited[cnt][x][y] + 1:
                        visited[cnt+1][nx][ny] = visited[cnt][x][y] + 1
                        d_que.append((nx,ny,cnt+1))
    return -1

N,M,K = map(int,input().split())
map = [list(map(int,input())) for _ in range(N)]
visited = [[[float('inf')]*M for _ in range(N)] for _ in range(K+1)]


print(BFS())
