# https://www.acmicpc.net/problem/2644
import sys
sys.stdin = open('input_2644.txt','r')

from collections import  deque

T = 2

def BFS(start,end):
    d_que = deque()
    d_que.append((a,1))
    while d_que:
        now,cnt = d_que.popleft()
        visited.add(now)
        for next_family in family[now]:
            if next_family == end: return cnt
            if next_family in visited: continue
            d_que.append((next_family,cnt+1))
    return -1


for test_case in range(1,T+1):
    N = int(input())
    a,b = map(int,input().split())
    M = int(input())
    family ={}
    for i in range(1,N+1):
        family[i] = set()
    for _ in range(M):
        p,c =map(int,input().split())
        family[p].add(c)
        family[c].add(p)
    visited = set()
    a = BFS(a,b)
    print(a)

