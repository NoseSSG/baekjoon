# https://www.acmicpc.net/problem/1068
import sys
sys.stdin = open('input_1068.txt','r')

from collections import deque

def BFS(start):
    global ans
    if start == delete:
        ans = 0
        return
    d_que = deque()
    d_que.append(start)
    while d_que:
        now = d_que.popleft()
        if not child[now]:
            ans += 1
        for next in child[now]:
            if next == delete:
                if len(child[now])==1: ans+=1
                continue
            d_que.append(next)


N = int(input())
num = list(map(int,input().split()))
child = [[] for _ in range(N)]
delete = int(input())
root = 0
for idx in range(N):
    if num[idx] == -1:
        root = idx
    else:
        child[num[idx]].append(idx)
ans = 0
BFS(root)
print(ans)
