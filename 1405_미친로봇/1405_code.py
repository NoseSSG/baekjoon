# https://www.acmicpc.net/problem/1405
import sys
sys.stdin = open('input_1405.txt','r')

def DFS(x,y,cnt,percent):
    global ans
    if cnt == N:
        ans += percent
        return
    visited.add((x,y))
    for d in range(4):
        nx,ny = x+dx[d], y+dy[d]
        if (nx,ny) in visited or not EWSN[d]:
            continue
        DFS(nx,ny,cnt+1,percent*(EWSN[d]/100))
        visited.discard((nx,ny))

T = 5
for test_case in range(1,T+1):
    temp = list(map(int,input().split()))
    N = temp[0]
    EWSN = temp[1:5]
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    visited = set()
    visited.add((0,0))
    ans = 0
    DFS(0,0,0,1)
    print(ans)