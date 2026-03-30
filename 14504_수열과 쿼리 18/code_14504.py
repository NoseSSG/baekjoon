# https://www.acmicpc.net/problem/14504
import sys
sys.stdin = open('input_14504.txt')
input = sys.stdin.readline
from bisect import bisect_right,insort
import math

N = int(input())
array = list(map(int,input().split()))
M = int(input())

blocks = []
block_size = int(math.sqrt(N))
for i in range(0,N,block_size):
    block = sorted(array[i:i+block_size])
    blocks.append(block)

for j in range(M):
    temp = list(map(int,input().split()))
    o = temp[0]

    if o == 1:
        _,i,j,k = temp
        i -= 1
        j -= 1
        ans = 0
        while i <= j and i % block_size != 0:
            if array[i] > k:
                ans+=1
            i+=1
        while i + block_size <= j:
            b = i//block_size
            ans += len(blocks[b]) - bisect_right(blocks[b],k)
            i += block_size
        while i <= j:
            if array[i] > k:
                ans += 1
            i += 1
        print(ans)
    else:
        _,i,k = temp
        i -= 1
        old = array[i]
        b = i //block_size
        blocks[b].remove(old)
        array[i] = k
        insort(blocks[b],k)