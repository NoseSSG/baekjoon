# https://www.acmicpc.net/problem/1012

import sys
sys.stdin = open('input_1012.txt','r')

from collections import deque


def BFS(now):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    d_que = deque()
    d_que.append(now)
    while d_que:
        (x,y) = d_que.popleft()
        for d in range(4):
            nx,ny = x+dx[d], y+dy[d]
            if (nx,ny) in plant:
                d_que.append((nx,ny))
                plant.discard((nx,ny))


T = int(input())
for test_case in range(T):
    N,M,K = map(int,input().split())
    plant = set()
    for _ in range(K):
        x,y = map(int,input().split())
        plant.add((x,y))
    ans = 0
    while True:
        if not plant:
            break
        now = plant.pop()
        BFS(now)
        ans += 1
    print(ans)