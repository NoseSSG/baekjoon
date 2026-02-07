# https://www.acmicpc.net/problem/1517
import sys
sys.stdin = open('input_1517.txt')
input = sys.stdin.readline
from math import ceil,log

N = int(input())
temp = list(map(int,input().split()))

sorted_temp = sorted(temp)

unique = []
prev = None
for v in sorted_temp:
    if prev != v:
        unique.append(v)
        prev = v

from bisect import bisect_left
rank = [bisect_left(unique,v) + 1 for v in temp]
M = len(unique)

seg_tree = [0]*2**(ceil(log(M,2)+1))

def update(node,s,e,idx):
    if idx < s or idx > e:
        return
    seg_tree[node] += 1
    if s == e:
        return
    mid = (s + e ) // 2
    update(node*2,s,mid,idx)
    update(node*2+1,mid+1,e,idx)

def query(node,s,e,l,r):
    if r < s or e < l:
        return 0
    if l <= s and e <= r:
        return seg_tree[node]
    mid = (s + e)//2
    return query(node*2,s,mid,l,r) + query(node*2+1,mid+1,e,l,r)

ans = 0
for x in rank:
    if x < M:
        ans += query(1,1,M,x+1,M)
    update(1,1,M,x)
print(ans)