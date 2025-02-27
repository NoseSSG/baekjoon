# https://www.acmicpc.net/problem/14225
import sys
sys.stdin = open('input_14225.txt')

N = int(input())
temp = list(map(int,input().split()))
ans = [0] * 2000000

def bit_mask(num):
    for i in range(1<<num):
        temp_arr = []
        for j in range(num):
            if i & (1<<j):
                temp_arr.append(temp[j])
        if temp_arr:
            ans[sum(temp_arr)] = 1
bit_mask(N)
for i in range(1,len(ans)+1):
    if not ans[i]:
        print(i)
        break