# https://www.acmicpc.net/problem/13305
import sys
sys.stdin = open('input_13305.txt')

N = int(input())
meter = list(map(int,input().split()))
price = list(map(int,input().split()))

ans = 0
min = 10**10
for i in range(N-1):
    if price[i] < min:
        min = price[i]
    ans += meter[i]*min
print(ans)