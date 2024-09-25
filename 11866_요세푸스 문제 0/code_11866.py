# https://www.acmicpc.net/problem/11866
import sys
sys.stdin = open('input_11866.txt','r')

from collections import deque

N,M = map(int,input().split())
ans = []
d_que = deque(list(range(1,N+1)))
while d_que:
    d_que.rotate(-2)
    ans.append(d_que.popleft())
print(f'< {d_que}')
