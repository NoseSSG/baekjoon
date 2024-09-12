# https://www.acmicpc.net/problem/11054
import sys
sys.stdin = open('input_11054.txt','r')

N = int(input())
temp = list(map(int,input().split()))
dp =[0]*N


for i in range(1,N):
    for j in range(i):
        if temp[i] > temp[j]:
            dp[i] = max(dp[j]+1,dp[i])

dp_back = [0] * N
temp_back = temp[::-1]
for i in range(1,N):
    for j in range(i):
        if temp_back[i] > temp_back[j]:
            dp_back[i] = max(dp_back[j]+1,dp_back[i])

ans = 0
for i in range(N):
    ans = max(ans,dp[i] + dp_back[::-1][i])
print(ans+1)