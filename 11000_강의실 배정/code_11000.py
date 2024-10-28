# https://www.acmicpc.net/problem/11000
import sys
sys.stdin = open('input_11000.txt','r')

import heapq

N = int(input())

class_time = [list(map(int,input().split())) for _ in range(N)]
class_time.sort()
h_que = []
heapq.heappush(h_que,class_time[0][1])

ans = 1
for i in range(1,N):
    a,b = class_time[i]
    if h_que[0] > a:
        ans += 1
        heapq.heappush(h_que,b)
    else:
        heapq.heappop(h_que)
        heapq.heappush(h_que,b)
print(ans)