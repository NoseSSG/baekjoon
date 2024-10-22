# https://acmicpc.net/problem/20040
import sys
# sys.stdin=open('input_20040.txt','r')

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


N,M = map(int,input().split())
ans = 0
spot = set()
parent = [i for i in range(N)]

for i in range(1,M+1):

    a,b = map(int,input().split())
    parent_a = find_parent(a)
    parent_b = find_parent(b)
    if parent_a == parent_b:
        ans = i
        break
    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b
print(ans)