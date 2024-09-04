# https://www.acmicpc.net/problem/25498
import sys
sys.stdin = open('input_25498.txt','r')
from collections import deque

def DFS(node,temp):
    global ans
    visited.add(node)
    d_que = deque()
    d_que.append((node,temp))
    while d_que:
        idx,str = d_que.popleft()
        visited.add(idx)
        max_idx = []
        max_char = ''
        for i in graph[idx]:
            if i in visited: continue
            if max_char < char[i]:
                max_idx = [i]
                max_char = char[i]
            elif max_char == char[i]:
                max_idx.append(i)
        if not max_idx:
            if ans < str+char[idx]: ans = str+char[idx]
        else:
            for i in max_idx:
                d_que.append((i,str+char[idx]))


N = int(input())
string = set()
graph = {}
char = list(map(str,input().rstrip()))
visited = set()
for _ in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    if a not in graph:
        graph[a] = set()
    if b not in graph:
        graph[b] = set()
    graph[a].add(b)
    graph[b].add(a)
ans = ''
DFS(0,'')
print(ans)
# answer = sorted(string,reverse=True)
# print(answer[0])