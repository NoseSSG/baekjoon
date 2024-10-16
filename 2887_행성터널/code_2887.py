# https://www.acmicpc.net/problem/2887
import sys

sys.stdin = open('input_2887.txt','r')

import heapq

def find_parent(n):
    if parent[n] != n:
        parent[n] = find_parent(parent[n])
        return parent[n]
    return n

N = int(input())
planet = [list(map(int,input().split())) for _ in range(N)]
parent = [t for t in range(N)]

h_que = []

x_sort = []
y_sort = []
z_sort = []


for i in range(N):
    x,y,z = planet[i]
    x_sort.append((x,i))
    y_sort.append((y,i))
    z_sort.append((z,i))
x_sort.sort()
y_sort.sort()
z_sort.sort()



for i in range(N-1):
    heapq.heappush(h_que,(abs(x_sort[i][0]-x_sort[i+1][0]),x_sort[i][1],x_sort[i+1][1]))
    heapq.heappush(h_que,(abs(y_sort[i][0]-y_sort[i+1][0]),y_sort[i][1],y_sort[i+1][1]))
    heapq.heappush(h_que,(abs(z_sort[i][0]-z_sort[i+1][0]),z_sort[i][1],z_sort[i+1][1]))

cnt = 0
ans = 0
while h_que:
    cost,a,b = heapq.heappop(h_que)
    a_par = find_parent(a)
    b_par = find_parent(b)
    if a_par == b_par:
        continue
    if a_par < b_par:
        parent[b_par] = a_par
    else:
        parent[a_par] = b_par
    ans += cost
    cnt += 1
    if cnt == N-1:
        break
print(ans)
