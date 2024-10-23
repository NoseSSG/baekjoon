# https://acmicpc.net/problem/1021
import sys
# sys.stdin = open('input_1021.txt','r')

from collections import deque

N,M = map(int,input().split())
temp_list = [i for i in range(1,N+1)]
d_que = deque(temp_list)
numbers = list(map(int,input().split()))
ans = 0
for number in numbers:
    while True:
        if d_que[0] == number:
            d_que.popleft()
            break
        if d_que.index(number) <= len(d_que)//2:
            ans += 1
            d_que.rotate(-1)
        else:
            ans += 1
            d_que.rotate(1)
print(ans)