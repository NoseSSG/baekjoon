# https://www.acmicpc.net/problem/11438
import sys
# sys.stdin = open('input_11438.txt')

input = sys.stdin.readline # 이거 안하면 시간초과
sys.setrecursionlimit(10**5) # 이거 안하면 시간초과

def DFS(node,dep):
    check[node] = True
    depth[node] = dep

    for next_node in graph[node]:
        if check[next_node]: continue
        parent[next_node][0] = node
        DFS(next_node,dep+1)

def set_parent():
    DFS(1,0)
    for i in range(1,LOG):
        for j in range(1,N+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def LCA(fir,sec):
    if depth[fir] > depth[sec]: fir,sec = sec,fir
    for i in range(LOG-1,-1,-1):
        if depth[sec] - depth[fir] >= (1 << i):
            sec = parent[sec][i] 
    if fir == sec: return fir

    for i in range(LOG-1,-1,-1):
        if parent[fir][i] != parent[sec][i]:
            fir = parent[fir][i]
            sec = parent[sec][i]
    return parent[fir][0]


LOG = 2 * 20

N = int(input())
graph = [[] for _ in range(N+1)]
parent = [[0]*(LOG) for _ in range(N+1)]
check = [False]*(N+1)
depth = [0]*(N+1)

for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

set_parent()

m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    print(LCA(a,b))