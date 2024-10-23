# https://www.acmicpc.net/problem/2357
import sys

sys.stdin = open('input_2357.txt','r')

def make_seg_tree(idx,start,end):
    if start==end:
        seg_tree[idx] = [num[start],num[start]]
        return seg_tree[idx]
    mid = (start+end) //2
    left_ = make_seg_tree(idx*2,start,mid)
    right_ = make_seg_tree(idx*2+1,mid+1,end)

    seg_tree[idx] = [min(left_[0],right_[0]),max(left_[1],right_[1])]
    return seg_tree[idx]

def find_seg_tree(idx,start,end,range1,range2):
    if range2 < start or end < range1:
        return [float('inf'),0]
    if range1 <= start and end <= range2:
        return seg_tree[idx]
    mid = (start+end) // 2
    left_ = find_seg_tree(idx*2,start,mid,range1,range2)
    right_ = find_seg_tree(idx*2+1,mid+1,end,range1,range2)

    return [min(left_[0],right_[0]),max(left_[1],right_[1])]


N,M = map(int,input().split())
num = [int(input()) for _ in range(N)]
seg_tree = [0] * N*4
choice = [list(map(int,input().split())) for _ in range(M)]
make_seg_tree(1,0,N-1)
for a,b in choice:
    print(*find_seg_tree(1,0,N-1,a-1,b-1))
