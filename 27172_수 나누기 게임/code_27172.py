# https://www.acmicpc.net/problem/27172
import sys

sys.stdin = open('input_27172.txt','r')
N = int(input())
num = list(map(int,input().split()))
max_num = max(num)
cnt_num = [0] * (max_num + 1)
S = set(num)
for i in num:
    if i == max_num: continue
    for n in range(i*2,max_num+1,i):
        if n in S:
            cnt_num[i] += 1
            cnt_num[n] -= 1
for i in num:
    print(cnt_num[i],end =' ')