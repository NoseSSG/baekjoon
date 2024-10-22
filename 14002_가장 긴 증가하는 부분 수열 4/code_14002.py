# https://www.acmicpc.net/problem/14002
import sys
# sys.stdin = open('input_14002.txt','r')

import bisect

N = int(input())
num = list(map(int,input().split()))
ans = []
find_idx = []
for i in num:
    idx = bisect.bisect_left(ans,i)
    if idx == len(ans):
        ans.append(i)
    else:
        ans[idx] = i
    find_idx.append(idx)
print(len(ans))
end = len(ans) - 1
ans = []
for i in range(N-1,-1,-1):
    if find_idx[i] == end:
        ans.append(num[i])
        end -= 1
print(*ans[::-1])

