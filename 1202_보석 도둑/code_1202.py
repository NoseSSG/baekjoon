# https://www.acmicpc.net/problem/1202
import sys
# sys.stdin = open('input_1202.txt','r')

import heapq

N,K = map(int,input().split())
h_que = []
use = [False]*N
ans = [0]*N
max_idx = 0
for _ in range(N):
    a,b = map(int,input().split())
    # heapq.heappush(h_que,(a,b))
    h_que.append((a,b))
h_que.sort()
bag = []
for _ in range(K):
    c = int(input())
    bag.append(c)
bag.sort(reverse=True)
for bag_idx in range(K):
    max_idx = 0
    bag_size = bag[bag_idx]
    for idx in range(N):
        if use[idx]: continue
        if h_que[idx][0] > bag_size:
            break
        if ans[bag_idx] <= h_que[idx][1]:
            ans[bag_idx] = h_que[idx][1]
            max_idx = idx
    use[max_idx] = True
print(sum(ans))