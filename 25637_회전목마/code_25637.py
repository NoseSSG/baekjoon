# https://www.acmicpc.net/problem/25637
import sys
# sys.stdin = open('input_25637.txt','r')

N = int(input())
people = list(map(int,input().split()))
people += people
ans = float('inf')
for i in range(N):
    ans_temp = 0
    idx = 0
    for j in range(N):
        for _ in range(people[i+j]):
            ans_temp += abs(j-idx)
            idx += 1
    ans = min(ans,ans_temp)
print(ans)