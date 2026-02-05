# https://www.acmicpc.net/problem/1275
import sys
from math import ceil,log
sys.stdin = open('input_1275.txt')
input = sys.stdin.readline

def make_seg_tree(left,right,i):
    if left == right:
        seg_tree[i] = temp[left]
        return seg_tree[i]
    
    mid = (left+right)//2
    seg_tree[i] = make_seg_tree(left,mid,i*2) + make_seg_tree(mid+1,right,i*2+1)
    return seg_tree[i]

def search(start,end,left,right,i):
    if end < left or start > right:
        return 0
    
    if left <= start and end <= right:
        return seg_tree[i]
    
    mid = (start + end) // 2
    return search(start,mid,left,right,i*2) + search(mid+1,end,left,right,i*2+1)

def update(start,end,idx,diff,i):
    if start > idx or idx > end:
        return
    seg_tree[i] += diff
    if start != end:
        mid = (start + end) // 2
        update(start,mid,idx,diff,i*2)
        update(mid+1,end,idx,diff,i*2+1)

N,K = map(int ,input().split())
temp = list(map(int,input().split()))
seg_tree = [0] * 2**(ceil(log(N,2)+1))

make_seg_tree(0,N-1,1)

for _ in range(K):
    x,y,a,b = map(int,input().split())

    l = min(x,y) - 1
    r = max(x,y) - 1
    print(search(0,N-1,l,r,1))
    diff = b - temp[a-1]
    temp[a-1] = b
    update(0,N-1,a-1,diff,1)