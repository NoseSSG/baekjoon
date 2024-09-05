# https://www.acmicpc.net/problem/10773

import sys
sys.stdin = open('input_10773.txt','r')

N = int(input())
temp = []
for _ in range(N):
    t = int(input())
    if t == 0:
        temp.pop()
    else:
        temp.append(t)
print(sum(temp))