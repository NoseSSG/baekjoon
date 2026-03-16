# https://www.acmicpc.net/problem/2516
import sys
sys.stdin = open('input_2516.txt')
input = sys.stdin.readline
from collections import deque

N = int(input())
monkeys = [[] for _ in range(N+1)]
for i in range(1,N+1):
    temp = list(map(int,input().split()))
    monkeys[i] = temp[1:]
    

cage = [-1] * (N+1)
for i in range(1,N+1):
    cage[i] = i %2

same = [0] * (N+1)

for i in range(1,N+1):
    cnt = 0
    for nxt in monkeys[i]:
        if cage[i] == cage[nxt]:
            cnt += 1
    same[i] = cnt

q = deque()
for i in range(1,N+1):
    if same[i] >= 2:
        q.append(i)

while q:
    now = q.popleft()
    if same[now] < 2:
        continue

    old = cage[now]
    cage[now] = (cage[now]+1)%2

    for nxt in monkeys[now]:
        if cage[nxt] == old:
            same[nxt] -= 1
        else:
            same[nxt] += 1
        if same[nxt] >= 2:
            q.append(nxt)
    
    same[now] = len(monkeys[now]) - same[now]

    if same[now] >= 2:
        q.append(now)
cage0 = []
cage1 = []
for i in range(1,N+1):
    if cage[i] == 0:
        cage0.append(i)
    else:
        cage1.append(i)

print(len(cage0),*cage0)
print(len(cage1),*cage1)