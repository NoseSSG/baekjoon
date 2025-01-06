# https://www.acmicpc.net/problem/15988
import sys
sys.stdin = open('input_15988.txt')

N = int(input())

DP = [0 for _ in range(1000001)]
DP[1] = 1
DP[2] = 2
DP[3] = 4

for i in range(4,1000001):
    DP[i] = DP[i-1]%1000000009 + DP[i-2]%1000000009 + DP[i-3]%1000000009

for _ in range(N):
    N = int(input())
    print(DP[N]%1000000009)