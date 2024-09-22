# https://www.acmicpc.net/problem/1806
import sys
sys.stdin = open('input_1806.txt','r')

N,S = map(int,input().split())
num = list(map(int,input().split()))

if sum(num) < S:
    print(0)
    exit()

start = 0
end = 0
sum_num = 0
len_num = len(num)
while True:
    if sum_num >= S:
        len_num = min(len_num, end - start)
        sum_num -= num[start]
        start += 1
    elif end == N:
        break
    else:
        sum_num += num[end]
        end += 1
print(len_num)