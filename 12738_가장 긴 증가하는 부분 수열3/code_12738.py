# https://www.acmicpc.net/problem/12738
import sys
# sys.stdin = open('input_12738.txt','r')

import bisect

N = int(input())
num = list(map(int,input().split()))
temp = []
for i in num:
    idx = bisect.bisect_left(temp,i)
    if idx == len(temp):
        temp.append(i)
    else:
        temp[idx] = i
print(len(temp))