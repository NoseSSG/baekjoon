# https://www.acmicpc.net/problem/14942
import sys
sys.stdin = open('input_14942.txt')

LOG = 21

def dfs(node):
    visited[node] = True
    for next_node,cost in tree[node]:
        if visited[next_node]:continue
        parents[next_node][0] = [node,cost]
        dfs(next_node)

def set_parent():
    dfs(1)
    for i in range(1,LOG):
        for j in range(1,N+1):
            parents[j][i] = [parents[parents[j][i-1][0]][i-1][0],parents[parents[j][i-1][0]][i-1][1]+parents[j][i-1][1]]

def find_ant(index,cost):
    for i in range(LOG-1,-1,-1):
        if parents[index][i][1] <= cost:
            cost -= parents[index][i][1]
            index = parents[index][i][0]
    print(index)

N = int(input())
ants = [int(input()) for _ in range(N)]
tree = [[] for _ in range(N+1)]
parents = [[[1,0] for _ in range(LOG)] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(N-1):
    a,b,c = map(int,input().split())
    tree[a].append([b,c])
    tree[b].append([a,c])

set_parent()

for i in range(N):
    find_ant(i+1,ants[i])