# https://www.acmicpc.net/problem/10868
import sys

sys.stdin = open('input_10868.txt','r')

def make_seg(idx,start,end):
    if start == end:
        seg_tree[idx] = num[start]
        return seg_tree[idx]
    # if start +1 == end:
    #     seg_tree[idx] = min(num[start],num[end])
    #     return seg_tree[idx]
    mid = (start+end)//2
    left_min = make_seg(idx*2, start, mid)
    right_min = make_seg((idx*2)+1, mid+1, end)
    seg_tree[idx] = min(left_min,right_min)
    return seg_tree[idx]

def find_seg(idx,start,end,left,right):
    if left > end or right < start:
        return float('inf')
    if left <= start and end <= right:
        return seg_tree[idx]
    mid = (start+end)//2
    left_min = find_seg(idx*2,start,mid,left,right)
    right_min = find_seg((idx*2)+1,mid+1,end,left,right)
    return min(left_min,right_min)


N,M = map(int,input().split())
num = [int(input()) for _ in range(N)]
range_list=[list(map(int,input().split())) for _ in range(M)]
seg_tree =[float('inf')] * N * 4
make_seg(1,0,N-1)
# print(seg_tree)
for a,b in range_list:
    print(find_seg(1,0,N-1,a-1,b-1))
