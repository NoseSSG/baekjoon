# https://www.acmicpc.net/problem/1987
import sys
sys.stdin = open('input_1987.txt','r')

T = 4

def DFS(x,y,cnt):
    global ans
    for d in range(4):
        nx,ny = x + dx[d], y + dy[d]
        if 0 <= nx < R and 0<= ny < C:
            if temp[nx][ny] not in visited:
                visited.add(temp[nx][ny])
                DFS(nx,ny,cnt+1)
                visited.remove(temp[nx][ny])
            else:

                ans = max(ans,cnt)
for test_case in range(1,T+1):
    R, C = map(int,input().split())
    temp = [list(map(str,input().rstrip())) for _ in range(R)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    visited = set()
    visited.add(temp[0][0])
    ans = 1
    DFS(0,0,1)
    print(ans)