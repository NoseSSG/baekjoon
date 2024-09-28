# https://www.acmicpc.net/problem/13023
import sys
sys.stdin = open('input_13023.txt','r')

def DFS(now,depth):
    global ans
    if depth == 4:
        ans = 1
        return
    for next in Graph[now]:
        if visited[next] == False:
            visited[next] = True
            DFS(next,depth+1)
            visited[next] = False
    visited[now] = False

N,M = map(int,input().split())
Graph = [[] for _ in range(N)]
visited = [False] * N
for _ in range(M):
    a,b = map(int,input().split())
    Graph[a].append(b)
    Graph[b].append(a)

ans = 0
for i in range(N):
    visited[i] = True
    DFS(i,0)
    if ans == 1:
        break
print(ans)