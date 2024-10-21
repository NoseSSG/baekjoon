# https://www.acmicpc.net/problem/6549
import sys

sys.stdin = open('input_6549.txt','r')

def divide(start,end):
    print(start,end)
    if start == end:
        return hist[start]
    if start + 1 == end:
        if hist[start] > hist[end]:
            return max(hist[end]*2,hist[start])
        else:
            return max(hist[start]*2,hist[end])
    mid = (start+end)//2
    left_idx = mid - 1
    right_idx = mid + 1
    left_box = divide(start,mid)
    right_box = divide(mid+1,end)
    mid_box = hist[mid]
    now_height = mid_box
    while start <= left_idx and right_idx <= end:
        if hist[left_idx] < hist[right_idx]:
            if hist[right_idx] < now_height:
                now_height = hist[right_idx]
            mid_box = max(mid_box,now_height*(right_idx-left_idx))
            right_idx += 1
        else:
            if hist[left_idx] < now_height:
                now_height = hist[left_idx]
            mid_box = max(mid_box,now_height*(right_idx-left_idx))
            left_idx -= 1

    while start <= left_idx:
        if hist[left_idx] < now_height:
            now_height = hist[left_idx]
        mid_box = max(mid_box,now_height*(right_idx-left_idx))
        left_idx -= 1
    while right_idx <= end:
        if hist[right_idx] < now_height:
            now_height = hist[right_idx]
        mid_box = max(mid_box,now_height*(right_idx-left_idx))
        right_idx += 1
    return max(left_box,right_box,mid_box)



while True:
    input_temp = list(map(int,input().split()))
    N = input_temp[0]
    if N == 0: break
    hist = input_temp[1:]
    seg_tree =[0] *N*4
    print(input_temp)
    print(divide(0,N-1))