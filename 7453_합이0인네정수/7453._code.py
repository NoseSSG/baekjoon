# https://www.acmicpc.net/problem/7453
import sys

sys.stdin = open('input_7453.txt','r')

N  = int(input())

arr = [ list(map(int,input().split())) for _ in range(N)]
rotate_arr = [[0]*N for _ in range(4)]
for i in range(N):
    for j in range(4):
        rotate_arr[j][N-i-1] = arr[i][j]
ans = 0
sum_ab = {}
for a in rotate_arr[0]:
    for b in rotate_arr[1]:
        if (a+b) not in sum_ab:
            sum_ab[a+b] = 1
        else: sum_ab[a+b] += 1

for c in rotate_arr[2]:
    for d in rotate_arr[3]:
        if -(c+d) in sum_ab: ans += sum_ab[-(c+d)]
print(ans)