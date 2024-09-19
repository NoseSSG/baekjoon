# https://www.acmicpc.net/problem/1697
import sys
sys.stdin = open('input_1697.txt')

from collections import deque

def BFS(start):
    d_que = deque()
    d_que.append(start)
    time[start] = 0
    while d_que:
        now = d_que.popleft()
        if now == K: return time[now]
        for i in [now-1,now+1,now*2]:
            if 0 <= i <= 100000 and time[i] == -1:
                time[i] = time[now] + 1
                d_que.append(i)

N,K = map(int,input().split())
time = [-1] * 100001
print(BFS(N))