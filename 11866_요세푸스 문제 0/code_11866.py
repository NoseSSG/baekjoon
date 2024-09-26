# https://www.acmicpc.net/problem/11866
import sys
# sys.stdin = open('input_11866.txt','r')

from collections import deque

N,M = map(int,input().split())
ans = []
d_que = deque(list(range(1,N+1)))
while d_que:
    d_que.rotate(-(M-1))
    ans.append(d_que.popleft())

ans = ', '.join(map(str,ans))
print(f'<{ans}>')