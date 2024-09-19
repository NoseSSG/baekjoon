# https://www.acmicpc.net/problem/2294
import sys
sys.stdin = open('input_2294.txt')

N ,K = map(int,input().split())
coin = [ int(input()) for _ in range(N)]
DP = [float('inf')] * (K+1)
for c in coin:
    for idx in range(c,K+1):
        if c == idx:
            DP[idx] = 1
            continue
        DP[idx] = min(DP[idx],DP[idx-c]+1)
if DP[K] == float('inf'):
    print(-1)
else:
    print(DP[K])