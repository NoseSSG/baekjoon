# https://www.acmicpc.net/problem/9527
import sys
from itertools import count

sys.stdin = open('input_9257.txt','r')

DP = {0:0,1:1,2:4,3:12}


def count_one(num):
    N = len(format(num,'b'))
    if num == 1 or num == 0:
        return num
    return DP[N-1] + count_one(num - 2**(N-1)) + (num - 2**(N-1))+1


start,end = map(int,input().split())
for i in range(4,len(format(end,'b'))+1):
    DP[i] = 2*DP[i-1] + 2**(i-1)
a = count_one(end)
b = count_one(start-1)
print(a - b)