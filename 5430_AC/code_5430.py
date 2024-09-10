# https://www.acmicpc.net/problem/5430
import sys
sys.stdin = open('input_5430.txt','r')
from collections import deque
import re
T = int(input())

for test_case in range(1,T+1):
    temp = list(map(str,input().rstrip()))
    N = int(input())
    d_que = deque()
    num = input()
    num = re.sub(',' ,' ',num)
    num = num[1:-1]
    num = list(map(int,num.split()))
    for i in num:
        d_que.append(i)
    reverse_flag  = 0
    ans = ''
    for order in temp:
        if order == 'R':
            reverse_flag = (reverse_flag+1)%2
        elif order == 'D':
            if not d_que:
                ans = 'error'
                break
            if reverse_flag: d_que.pop()
            else: d_que.popleft()
    if ans == 'error':
        print(ans)
    else:
        if reverse_flag: d_que.reverse()
        print('[',end='')
        for i in range(len(d_que)):
            print(d_que[i],end='')
            if i != len(d_que)-1:
                print(',',end='')
        print(']')
