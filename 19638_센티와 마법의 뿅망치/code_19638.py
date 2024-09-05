# https://www.acmicpc.net/problem/19638
import sys
# sys.stdin = open('input_19638.txt','r')
import heapq
N, H, T = map(int,input().split())
temp = []
cnt = 0
for _ in range(N):
    heapq.heappush(temp,-int(input()))
for i in range(T):
    height = -heapq.heappop(temp)
    if height < H or height==1:
        heapq.heappush(temp,-height)
        break
    height //= 2
    heapq.heappush(temp,-height)
    cnt += 1
max_height = -heapq.heappop(temp)
if max_height >= H:
    print('NO')
    print(max_height)
else:
    print('YES')
    print(cnt)
