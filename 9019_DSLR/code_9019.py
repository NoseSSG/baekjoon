# https://www.acmicpc.net/problem/9019
import sys
sys.stdin = open('input_9019.txt','r')

from collections import deque

def change_num(num,o):
    if o == 'D':
        return (num*2)%10000
    if o == 'S':
        num -= 1
        if num < 0: num = 9999
        return num
    if o == 'L':
        return (num%1000)*10 + num//1000
    if o == 'R':
        return num//10 + (num%10)*1000


def find_ans(a):
    d_que = deque()
    d_que.append((a,[]))
    visited[a] = True
    while d_que:
        now,orders = d_que.popleft()
        if now == B:
            return orders
        for d in order:
            temp = change_num(now,d)
            if visited[temp]:continue
            d_que.append((temp,orders+[d]))
            visited[temp] = True


T = int(input())
for test_case in range(1,T+1):
    A,B = map(int,input().split())
    visited = [False]*10000
    order = ['D','S','L','R']
    ans = find_ans(A)
    print(*ans,sep='')
    # print(change_num(1000,'L'))