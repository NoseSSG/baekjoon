# https://www.acmicpc.net/problem/9205
import sys
sys.stdin = open('input_9205.txt','r')

from collections import deque

T = int(input())

def BFS(s):
    d_que = deque()
    d_que.append(s)
    while d_que:
        now_x,now_y = d_que.popleft()
        if abs(end[0]-now_x)+abs(end[1] - now_y) <=1000:
            return "happy"
        for i in range(len(beer)):
            if not visited[i]:
                if abs(beer[i][0]-now_x)+abs(beer[i][1] - now_y) <=1000:
                    visited[i] = True
                    d_que.append(beer[i])
    return "sad"
for test_case in range(1,T+1):
    N = int(input())
    start = list(map(int,input().split()))
    beer = [list(map(int,input().split())) for _ in range(N)]
    end = list(map(int,input().split()))
    visited = [False]*len(beer)
    print(BFS(start))