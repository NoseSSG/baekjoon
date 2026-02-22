# https://www.acmicpc.net/problem/2629
import sys
sys.stdin = open('input_2629.txt')
input = sys.stdin.readline

N = int(input())
weights = list(map(int,input().split()))
M = int(input())
balls = list(map(int,input().split()))

total = sum(weights)
DP = ['N'] * (total+1)
DP[0] = ['Y']

for weight in weights:
    next_dp = DP[:]
    for d in range(total+1):
        if DP[d]=='N':
            continue
        if d + weight <= total:
            next_dp[d+weight] = 'Y'
        next_dp[abs(d-weight)] = 'Y'
    DP = next_dp

for ball in balls:
    if ball <= total:
        print(DP[ball],end=' ')
    else:
        print('N',end=' ')