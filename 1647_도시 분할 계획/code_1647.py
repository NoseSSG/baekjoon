# https://www.acmicpc.net/problem/1647
import sys
sys.stdin = open('input_1647.txt','r')

def find_parent(idx):
    if idx != union[idx]:
        union[idx] = find_parent(union[idx])
    return union[idx]


N,M = map(int,input().split())
edges = []
union = [i for i in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
edges.sort()
ans = 0
max_cost = 0
for edge in edges:
    cost,node1,node2 = edge
    p_node1 = find_parent(node1)
    p_node2 = find_parent(node2)
    if p_node1 == p_node2:
        continue
    if p_node1 < p_node2:
        union[p_node2] = p_node1
    else:
        union[p_node1] = p_node2
    ans += cost
    max_cost = max(max_cost,cost)
print(ans - max_cost)



