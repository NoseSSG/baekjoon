# https://www.acmicpc.net/problem/4195
import sys
sys.stdin =open('input_4195.txt','r')

def find_parent(x):
    if name[x] == x:
        return x
    name[x] = find_parent(name[x])
    return name[x]



def union(x,y):
    x_parent = find_parent(x)
    y_parent = find_parent(y)
    if x_parent == y_parent:
        return
    name[y_parent] = x_parent
    count[x_parent] += count[y_parent]



T = int(input())
for _ in range(T):
    N = int(input())
    name = {}
    count = {}
    for _ in range(N):
        A,B = map(str,input().split())
        if A not in name:
            name[A] = A
            count[A] = 1
        if B not in name:
            name[B] = B
            count[B] = 1
        union(A,B)
        print(count[find_parent(A)])
