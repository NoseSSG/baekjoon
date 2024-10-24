# https://www.acmicpc.net/problem/4485
import sys
sys.stdin = open('input_4485.txt','r')

import heapq

def BFS():
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    cnt=[[float('inf')]*N for _ in range(N)]
    h_que = []
    heapq.heappush(h_que,(cave[0][0],(0,0)))
    cnt[0][0] = cave[0][0]
    while h_que:
        minus_rupee,(x,y) = heapq.heappop(h_que)
        if (x,y) == (N-1,N-1):
            return minus_rupee
        if minus_rupee > cnt[x][y]:
            continue
        for d in range(4):
            nx,ny = x+dx[d],y+dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                temp_sum = minus_rupee + cave[nx][ny]
                if temp_sum < cnt[nx][ny]:
                    cnt[nx][ny] = temp_sum
                    heapq.heappush(h_que,(temp_sum,(nx,ny)))



test_case = 1
while True:
    N = int(input())
    if N == 0:break
    cave = [list(map(int,input().split())) for _ in range(N)]
    ans = BFS()
    print(f'Problem {test_case}: {ans}')