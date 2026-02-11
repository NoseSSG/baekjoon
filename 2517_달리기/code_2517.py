# https://www.acmicpc.net/problem/2517
import sys
sys.stdin = open('input_2517.txt')
input = sys.stdin.readline

def update(i):
    while i <= N:
        seg_tree[i] += 1
        i += i & -i

def prefix_sum(i):
    s = 0
    while i > 0:
        s += seg_tree[i]
        i -= i & -i
    return s

    
N = int(input())
temp = [int(input()) for _ in range(N)]
idx = list(range(N))
idx.sort(key=temp.__getitem__)
ranks = [0] * N
r = 1
for pos in idx:
    ranks[pos] = r
    r += 1

seg_tree = [0] * (4 * N) 

for i in range(N):
    r = ranks[i]
    print(i - prefix_sum(r) + 1)
    update(r)
