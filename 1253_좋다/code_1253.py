# https://www.acmicpc.net/problem/1253
import sys
sys.stdin = open('input_125.txt')

N = int(input())
num = list(map(int,input().split()))
num.sort()
ans = 0
for idx in range(N):
    start = 0
    end = N-1
    while True:
        if start == end:
            break
        if num[start] + num[end] == num[idx]:
            if start == idx:
                start += 1
            elif end == idx:
                end -= 1
            else:
                ans += 1
                break
        elif num[start] + num[end] > num[idx]:
            end -= 1
        else:
            start += 1
print(ans)