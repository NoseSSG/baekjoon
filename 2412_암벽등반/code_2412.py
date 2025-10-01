# https://www.acmicpc.net/problem/2412
import sys
sys.stdin = open('input_2412.txt')

from collections import deque

n,T = map(int,input().split())

dot = set()

for _ in range(n):
    x,y = map(int,input().split())
    dot.add((x,y))

d_que = deque()
d_que.append((0,0,0))
flag = False
while d_que:
    x,y,count = d_que.popleft()
    if y == T:
        flag =True
        break
    
    for i in range(-2,3):
        for j in range(-2,3):
            if(x+i,y+j) in dot:
                d_que.append((x+i,y+j,count+1))
                dot.remove((x+i,y+j))

print(count if flag else -1)