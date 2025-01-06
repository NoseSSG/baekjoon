# https://www.acmicpc.net/problem/5525
import sys
sys.stdin = open("input_5525.txt")

N = int(input())
M = int(input())

temp = input()
i = 0
count = 0
ans = 0
while i < M:
    if temp[i:i+3] == 'IOI':
        count += 1
        i += 2
        if count == N:
            ans += 1
            count -= 1
        
    else:
        i += 1
        count = 0
print(ans)