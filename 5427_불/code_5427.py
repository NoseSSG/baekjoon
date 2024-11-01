# https://www.acmicpc.net/problem/5427
import sys

sys.stdin = open('input_5427.txt','r')

from collections import deque

def BFS():
    d_que = deque()
    d_que.append((human[0],'@'))
    visited = [[float('inf')]*N for _ in range(M)]
    visited[human[0][0]][human[0][1]] = 0
    for fire in fires:
        d_que.append((fire,'*'))

    while d_que:
        (cx,cy),status = d_que.popleft()
        if status != building[cx][cy]:
            continue
        if (cx==0 or cx==M-1 or cy == 0 or cy ==N-1) and status == '@':
            return visited[cx][cy] + 1
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = cx+dx, cy+dy
            if 0 <= nx < M and 0 <= ny < N:
                if status == '@':
                    if building[nx][ny]=='.' and visited[nx][ny] > visited[cx][cy] +1:
                        visited[nx][ny] = visited[cx][cy] +1
                        building[nx][ny] = status
                        d_que.append(((nx,ny),status))
                elif status == '*':
                    if building[nx][ny] == '.' or building[nx][ny] =='@':
                        building[nx][ny] = status
                        d_que.append(((nx,ny),status))
    return "IMPOSSIBLE"



T = int(input())

for test_case in range(T):
    N,M = map(int,input().split())
    building = [list(map(str,input())) for _ in range(M)]
    fires = []
    human = []
    for i in range(M):
        for j in range(N):
            if building[i][j] == '@':
                human.append((i,j))
            elif building[i][j] == '*':
                fires.append((i,j))
    print(BFS())