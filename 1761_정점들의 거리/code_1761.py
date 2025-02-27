# https://www.acmicpc.net/problem/1761
import sys
sys.stdin = open('input_1761.txt')
sys.setrecursionlimit(100000)

def set_depth(node,dep):
    depthes[node] = dep
    check[node] =  True

    for next,price in graph[node]:
        if check[next]: continue
        parent[next][0] = node
        dist[next] = dist[node] + price
        set_depth(next,dep+1)

def set_parent():
    set_depth(1,0)

    for i in range(1,LOG):
        for j in range(1,N+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def LCA(fir,sec):
    if depthes[fir] > depthes[sec]: fir,sec = sec,fir
    for i in range(LOG-1,-1,-1):
        if depthes[sec] - depthes[fir] >= (1<<i):
            sec = parent[sec][i]
    if fir == sec:
        return fir
    
    for i in range(LOG-1,-1,-1):
        if parent[fir][i] != parent[sec][i]:
            fir = parent[fir][i]
            sec = parent[sec][i]
    return parent[fir][0]



LOG = 17
N = int(input())
graph = [[] for _ in range(N+1)]
depthes = [0] * (N+1)
check = [False] * (N+1)
dist = [0] * (N+1)
parent = [[0] *LOG for _ in range(N+1)]


for _ in range(N-1):
    a,b,c= map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

set_parent()

M = int(input())
for _ in range(M):
    a,b = map(int,input().split())
    print(dist[a]+dist[b]-2*dist[LCA(a,b)])