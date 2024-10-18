# https://www.acmicpc.net/problem/3109
import sys
# sys.stdin = open('input_3109.txt')

def DFS(x,y):
    global ans
    if y == M-1:
        ans +=1
        return True
    for d in range(3):
        nx,ny = x+dx[d], y+1
        if 0 <= nx < N and 0 <= ny < M:
            if gas[nx][ny] == '.':
                gas[nx][ny] = 'x'
                temp = DFS(nx,ny)
                if temp:
                    return True
    return False

N,M = map(int,input().split())
gas = [list(map(str,input())) for _ in range(N)]
dx = [-1,0,1]
ans = 0
for i in range(N):
    DFS(i,0)
print(ans)