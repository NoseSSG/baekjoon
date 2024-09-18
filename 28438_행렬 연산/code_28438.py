# https://www.acmicpc.net/problem/28438
import sys
sys.stdin = open('input_28439.txt','r')

N,M,Q = map(int,input().split())
row = [0] * M
cal = [0] * N
for _ in range(Q):
    a,b,c = map(int,input().split())
    if a == 1:
        cal[b-1] += c
    elif a == 2:
        row[b-1] += c
for i in range(N):
    for j in range(M):
        print(cal[i]+row[j],end=' ')
    print()