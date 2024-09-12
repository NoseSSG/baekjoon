# https://www.acmicpc.net/problem/17404
import sys
# sys.stdin = open('input_17404.txt','r')

N = int(input())
value = [list(map(int,input().split())) for _ in range(N)]

ans = [float('inf')] * 3
for start in range(3):
    DP = [[float('inf')]*3 for _ in range(N)]
    DP[0][start] = value[0][start]
    for now in range(1,N):
        DP[now] = [min(DP[now-1][1],DP[now-1][2])+value[now][0],
                   min(DP[now-1][0],DP[now-1][2])+value[now][1],
                   min(DP[now-1][0],DP[now-1][1])+value[now][2]]
    for check in range(3):
        if start != check:
            ans[check] = min(ans[check],DP[-1][check])
print(min(ans))
