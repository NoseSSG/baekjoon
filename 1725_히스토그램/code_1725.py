# https://www.acmicpc.net/problem/1725
import sys
sys.stdin = open('input_1725.txt','r')

def make_seg(idx,start,end):
    if start==end:
        seg_tree[idx] = height[start]
        return seg_tree[idx]
    if start +1  == end:
        seg_tree[idx] = max(min(height[start],height[end])*2,max(height[start],height[end]))
        return seg_tree[idx]
    mid = (start+end)//2
    left_idx = mid-1
    right_idx = mid +1
    left_box = make_seg(idx*2,start,mid)
    right_box = make_seg(idx*2+1,mid+1,end)
    mid_box = height[mid]
    now_height = mid_box
    while start <= left_idx and right_idx <= end:
        if height[left_idx] < height[right_idx]:
            if height[right_idx] < now_height:
                now_height = height[right_idx]
            mid_box = max(mid_box,now_height*(right_idx - left_idx))
            right_idx += 1
        else:
            if height[left_idx] < now_height:
                now_height = height[left_idx]
            mid_box = max(mid_box,now_height*(right_idx-left_idx))
            left_idx -= 1

    while start <= left_idx:
        if height[left_idx] < now_height:
            now_height = height[left_idx]
        mid_box = max(mid_box,now_height*(right_idx-left_idx))
        left_idx -= 1

    while right_idx <= end:
        if height[right_idx] < now_height:
            now_height = height[right_idx]
        mid_box = max(mid_box,now_height*(right_idx-left_idx))
        right_idx += 1
    # print(start,end,left_box,mid_box,right_box)
    # print()
    return max(mid_box,left_box,right_box)

N = int(input())
height = [int(input()) for _ in range(N)]
seg_tree = [0]*N*4
# make_seg(1,0,N-1)
print(make_seg(1,0,N-1))
