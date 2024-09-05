# https://www.acmicpc.net/problem/1967
import sys
sys.stdin = open('input_1967.txt','r')

from collections import deque
def BFS(start):
    d_que = deque()
    d_que.append((start,0))
    while d_que:
        now,dist = d_que.popleft()
        visited[now] = dist
        if now not in tree:continue
        for next,edge in tree[now]:
            if visited[next] == -1:

                visited[next] = dist + edge
                d_que.append((next,visited[next]))

N = int(input())
tree = {}
for _ in range(N-1):
    a,b,c = map(int,input().split())
    if a not in tree:
        tree[a] = set()
    if b not in tree:
        tree[b] = set()
    tree[a].add((b,c))
    tree[b].add((a,c))
visited = [-1] * (N+1)
BFS(1)
max_idx = visited.index(max(visited))
visited = [-1] * (N+1)
BFS(max_idx)
print(max(visited))
