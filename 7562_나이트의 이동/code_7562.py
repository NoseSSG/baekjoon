# https://www.acmicpc.net/problem/7562
import sys
sys.stdin = open('input_7562.txt','r')

from collections import deque

def BFS(start):
    d_que = deque()

    d_que.append((0,start))
    visited.add(start)
    while d_que:
        cnt,(x,y) = d_que.popleft()
        if (x,y) == end:
            return cnt
        for d in range(8):
            nx,ny = x+dx[d],y+dy[d]
            if 0<= nx < N and 0 <= ny < N and (nx,ny) not in visited:
                d_que.append((cnt+1,(nx,ny)))
                visited.add((nx,ny))

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    start = tuple(map(int,input().split()))
    end = tuple(map(int,input().split()))
    dx = [-1,-2,-2,-1,1,2,2,1]
    dy = [-2,-1,1,2,2,1,-1,-2]
    visited = set()
    print(BFS(start))