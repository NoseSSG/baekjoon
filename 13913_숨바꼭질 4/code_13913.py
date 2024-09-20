# https://www.acmicpc.net/problem/13913
import sys
sys.stdin = open('input_13913.txt','r')

from collections import deque

def print_route(end):
    now = end
    cnt_ = time[end]
    ans = deque()
    ans.append(end)
    for _ in range(cnt_):
        ans.appendleft(before[now])
        now = before[now]
    print(*ans)


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
                before[i] = now

N,K = map(int,input().split())
time = [-1] * 100001
before = [-1] * 100001
cnt = BFS(N)
print(cnt)
print_route(K)