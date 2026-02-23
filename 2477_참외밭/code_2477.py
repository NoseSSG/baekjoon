# https://www.acmicpc.net/problem/2477
import sys
sys.stdin = open('input_2477.txt')
input = sys.stdin.readline

K = int(input())

max_h = max_w = x = y = 0
lines = []
for i in range(6):
    temp = list(map(int,input().split()))
    lines.append(temp[1])
    if temp[0] < 3:
        # 가로선
        if temp[1] > max_w:
            max_w = temp[1]
            x = i
    else:
        # 세로선
        if temp[1] > max_h:
            max_h = temp[1]
            y = i

min_w = abs(lines[(x-1)%6] - lines[(x+1)%6])
min_h = abs(lines[(y-1)%6] - lines[(y+1)%6])

area = max_h*max_w - min_h*min_w

print(area * K)