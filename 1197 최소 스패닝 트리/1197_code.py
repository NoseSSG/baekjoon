# https://www.acmicpc.net/problem/1197
import sys
sys.stdin = open('input_1197.txt','r')

import heapq

def find_head(x):
    if dict[x] != x:
        dict[x] = find_head(dict[x])
    return dict[x]

V,E = map(int,input().split())

temp = []
dict = {}
for i in range(1,V+1):
    dict[i] = i

ans = 0
for _ in range(E):
    v1,v2,e = map(int,input().split())
    heapq.heappush(temp,(e,v1,v2))

while temp:
    e,v1,v2 = heapq.heappop(temp)
    v1_head = find_head(v1)
    v2_head = find_head(v2)
    if v1_head == v2_head:
        continue
    ans += e
    if v1_head < v2_head:
        dict[v2_head] = v1_head
    else:
        dict[v1_head] = v2_head
print(ans)