# https://www.acmicpc.net/problem/2295
import sys
sys.stdin = open('input_2295.txt','r')

N = int(input())
num = [int(input()) for _ in range(N)]
num.sort()
A = set()
for a in num:
    for b in num:
        A.add(a+b)
for i in range(N-1,-1,-1):
    for j in range(i+1):
        if num[i] - num[j] in A:
            print(num[i])
            exit()