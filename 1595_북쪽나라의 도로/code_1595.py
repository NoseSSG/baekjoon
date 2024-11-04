# https://www.acmicpc.net/problem/1595
import sys

sys.stdin = open('input_1595.txt','r')

def DFS(node,length):
    global ans
    global node_idx
    visited.add(node)
    for [next_node,edge] in graph[node]:
        if next_node not in visited:
            ans = max(ans,length+edge)
            if ans == length+edge: node_idx = next_node
            DFS(next_node,length+edge)


graph = {}
while True:
    try:
        a,b,c = map(int,input().split())
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append([b,c])
        graph[b].append([a,c])
    except:
        if not graph:
            print(0)
            exit()
        break

ans = 0
node_idx = 0
visited = set()
DFS(1,0)
ans = 0
visited.clear()
DFS(node_idx,0)
print(ans)
