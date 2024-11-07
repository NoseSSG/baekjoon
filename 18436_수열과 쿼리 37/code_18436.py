# https://www.acmicpc.net/problem/18436
import sys

sys.stdin = open('input_18436.txt','r')

def make_seg(idx,start,end):

    if start == end:
        if num[start] % 2 == 0:
            seg_tree[idx] = [1,0]
        else:
            seg_tree[idx] = [0,1]
        return seg_tree[idx]
    # if start + 1 == end:
    #     pass

    mid = (start+end)//2
    left_odd,left_even = make_seg(idx*2,start,mid)
    right_odd,right_even = make_seg(idx*2+1,mid+1,end)

    seg_tree[idx] = [left_odd+right_odd,left_even+right_even]
    return seg_tree[idx]

def update_seg(idx,start,end,target_idx,even_odd):
    if start > target_idx or end < target_idx:
        return
    if start == end:
        result = [a + b for a, b in zip(seg_tree[idx], even_odd)]
        seg_tree[idx] = result
        return
    if start <= target_idx <= end:
        result = [a+b for a,b in zip(seg_tree[idx],even_odd)]
        seg_tree[idx] = result
        # return
    mid = (start+end)//2
    update_seg(idx*2,start,mid,target_idx,even_odd)
    update_seg(idx*2+1,mid+1,end,target_idx,even_odd)

def find_even_odd(idx,start,end,left,right):
    if start > right or end < left:
        return[0,0]
    if left<=start and end <= right:
        return seg_tree[idx]
    mid = (start+end)//2
    left_count = find_even_odd(idx*2,start,mid,left,right)
    right_count = find_even_odd(idx*2+1,mid+1,end,left,right)
    # print(left_count,right_count)
    return [a+b for a,b in zip(left_count,right_count)]




N = int(input())
num = list(map(int,input().split()))
M = int(input())

seg_tree = [[0,0]] * N * 4
make_seg(1,0,N-1)


for _ in range(M):
    a,b,c, = map(int,input().split())
    if a == 1:
        if c % 2 == num[b-1] % 2:
            num[b-1] = c
            continue
        else:
            num[b-1] = c
            if c%2==1:
                update_seg(1,0,N-1,b-1,[-1,1])
            else:
                update_seg(1,0,N-1,b-1,[1,-1])
    else:
        ans = find_even_odd(1,0,N-1,b-1,c-1)
        if a == 2: print(ans[0])
        else: print(ans[1])
