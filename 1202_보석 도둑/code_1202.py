# https://www.acmicpc.net/problem/1202
import sys
# sys.stdin = open('input_1202.txt','r')

import heapq

N,K = map(int,input().split())
h_que = []
for _ in range(N):
    a,b = map(int,input().split())
    heapq.heappush(h_que,(a,b))

bag = []
for _ in range(K):
    c = int(input())
    bag.append(c)
bag.sort()
choice = []
ans = 0
for select_bag in bag:
    while h_que and h_que[0][0] <= select_bag:
        heapq.heappush(choice,-heapq.heappop(h_que)[1])
    if choice:
        ans += -heapq.heappop(choice)

print(ans)