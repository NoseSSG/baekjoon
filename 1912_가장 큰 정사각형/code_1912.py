# https://www.acmicpc.net/problem/1915
import sys
sys.stdin = open('input_1912.txt')

N,M = map(int,input().split())

temp = [list(map(int,input().rstrip())) for _ in range(N)]

DP = [[0]*M for _ in range(N)]

ans = 0

for i in range(N):
    for j in range(M):
        if i==0 or j==0:
            DP[i][j] = temp[i][j]
        elif temp[i][j] == 0:
            DP[i][j] = 0
        else:
            DP[i][j] = min(DP[i-1][j-1],DP[i][j-1],DP[i-1][j]) + 1

        ans = max(ans,DP[i][j])
print(ans**2)
        