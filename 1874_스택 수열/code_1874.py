# https://www.acmicpc.net/problem/1874
import sys
sys.stdin = open('input_1874.txt')
input = sys.stdin.readline

N = int(input())
temp = [int(input()) for _ in range(N)]
ans = []
stack = []
now = 1
for idx in range(N):
    while now <= temp[idx]:
        ans.append('+')
        stack.append(now)
        now += 1
    if temp[idx] == stack[-1]:
        ans.append('-')
        stack.pop()
    else:
        ans = ['NO']
        break
for x in ans:
    print(x)
    
    