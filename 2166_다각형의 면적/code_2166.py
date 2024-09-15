# https://www.acmicpc.net/problem/2166
import sys
sys.stdin = open('input_2166.txt','r')

N = int(input())
temp_x = []
temp_y = []
for _ in range(N):
    a,b = map(int,input().split())
    temp_x.append(a)
    temp_y.append(b)
temp_x.append(temp_x[0])
temp_y.append(temp_y[0])
xy = yx = 0
for i in range(N):
    xy += temp_x[i]*temp_y[i+1]
    yx += temp_y[i]*temp_x[i+1]
print(round(abs(xy-yx)/2,1))