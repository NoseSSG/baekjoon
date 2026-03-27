# https://www.acmicpc.net/problem/17410
import sys
sys.stdin = open('input_17410.txt')
input = sys.stdin.readline
from bisect import bisect_right, bisect_left, insort
import math

N = int(input())
array = list(map(int,input().split()))

block_size = int(math.sqrt(N))
blocks = []
for i in range(0,N,block_size):
    block = sorted(array[i:i+block_size])
    blocks.append(block)

M = int(input())

for _ in range(M):
    temp = list(map(int,input().split()))
    
    if temp[0]==1:
        k,target,num = temp
        target -= 1
        b = target//block_size
        old = array[target]

        pos = bisect_right(blocks[b],old)-1
        blocks[b].pop(pos)

        insort(blocks[b],num)
        array[target] = num

        
    else:
        k,left,right,num = temp
        left -= 1
        right -= 1
        
        ans = 0
        while left <= right and left % block_size !=0:
            if array[left] > num:
                ans += 1
            left += 1
        
        while left + block_size -1 <= right:
            b = left // block_size
            ans += len(blocks[b]) - bisect_right(blocks[b],num)
            left += block_size

        while left <= right:
            if array[left] > num:
                ans += 1
            left += 1
        print(ans)