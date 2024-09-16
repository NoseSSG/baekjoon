# https://www.acmicpc.net/problem/11399
import sys
sys.stdin = open('input_11399.txt')

N = int(input())
num = list(map(int,input().split()))
num.sort()
ans = 0
sum_time =0
for time in num:
    ans += sum_time + time
    sum_time += time
print(ans)