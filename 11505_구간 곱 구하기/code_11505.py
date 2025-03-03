# https://www.acmicpc.net/problem/11505
import sys
sys.stdin = open('input_11505.txt')

def make_seg(start,end,index):
    if start == end:
        seg_tree[index] = temp[start]
        return seg_tree[index]
    
    mid = (start + end) // 2
    seg_tree[index] = (make_seg(start,mid,index*2) * make_seg(mid+1,end,index*2+1)) % 1000000007
    return seg_tree[index]

def update_seg(start,end,index,target,num):
    if start == end:
        if start == target:
            seg_tree[index] = num
        return seg_tree[index]
    mid = (start + end) // 2
    seg_tree[index] = (update_seg(start,mid,index*2,target,num) * update_seg(mid+1,end,index*2+1,target,num)) % 1000000007
    return seg_tree[index]

def print_seg(start,end,index,left,right):
    if end < left or start > right:
        return 1
    if left <= start and end <= right:
        return seg_tree[index]
    mid = (start + end ) // 2
    return (print_seg(start,mid,index*2,left,right)*print_seg(mid+1,end,index*2+1,left,right)) % 1000000007
    

N,M,K = map(int,input().split())
seg_tree = [0] * N * 4
temp = [] 
for _ in range(N):
    temp.append(int(input()))

make_seg(0,N-1,1)

for _ in range(M+K):
    a,b,c = map(int,input().split())
    if a == 1:
        update_seg(0,N-1,1,b-1,c)
    else:
        print(print_seg(0,N-1,1,b-1,c-1))