# https://www.acmicpc.net/problem/1660
import sys
sys.stdin = open('input_1660.txt')

N = int(input())
bomb = []
num = 0
i = 1
while num < N:
    num += (i*(i+1))//2
    bomb.append(num)
    i += 1

dp = [float('inf')]*(N+1)
for cnt in range(1,N+1):
    for now in bomb:
        if cnt == now:
            dp[cnt] = 1
            break
        if now > cnt:
            break
        dp[cnt] = min(dp[cnt],dp[cnt-now]+1)
print(dp[N])