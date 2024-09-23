# https://www.acmicpc.net/problem/14719
import sys
# sys.stdin = open('input_14719.txt','r')

H,W = map(int,input().split())
block = list(map(int,input().split()))
ans = 0

for idx in range(1,W-1):
    left = max(block[:idx])
    right = max(block[idx+1:])

    max_h = min(left,right)
    if max_h > block[idx]:
        ans += max_h - block[idx]
print(ans)




