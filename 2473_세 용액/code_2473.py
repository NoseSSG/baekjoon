# https://www.acmicpc.net/problem/2473
import sys
# sys.stdin = open('input_2473.txt')

N = int(input())
temp = list(map(int,input().split()))
temp.sort()
min_sum = float('inf')
for idx in range(N-2):
    first = temp[idx]
    left_idx = idx+1
    right_idx = N-1
    while True:
        if left_idx >= right_idx:break
        sum_temp = first + temp[left_idx] + temp[right_idx]
        if abs(sum_temp) < abs(min_sum):
            min_sum = sum_temp
            ans = [first,temp[left_idx],temp[right_idx]]
        if sum_temp < 0: left_idx += 1
        elif sum_temp > 0: right_idx -= 1
        else:
            print(*ans)
            exit()

print(*ans)
