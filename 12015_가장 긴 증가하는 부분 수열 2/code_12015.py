# https://www.acmicpc.net/problem/12015
import sys
sys.stdin = open('input_12015.txt','r')

import bisect

N = int(input())
num = list(map(int,input().split()))
ans = []
for i in num:
    idx = bisect.bisect_left(ans,i)
    if idx == len(ans):
        ans.append(i)
    else:
        ans[idx] = i
print(len(ans))