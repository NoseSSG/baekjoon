# https://www.acmicpc.net/problem/15681
import sys
sys.stdin = open('input_15681.txt')

def make_tree(node,depth):
    depthes[node] = depth
    checkes[node] = True
    count[node] = 1
    for next_node in tree[node]:
        if checkes[next_node]: continue
        count[node] += make_tree(next_node,depth+1)
    return count[node]

N,R,Q = map(int,input().split())

tree = [[] for _ in range(N+1)]
depthes = [0] * (N+1)
checkes = [False] * (N+1)
count = [0] * (N+1)
for _ in range(N-1):
    U,V = map(int,input().split())
    tree[U].append(V)
    tree[V].append(U)

make_tree(R,0)

for _ in range(Q):
    start = int(input())
    print(count[start])