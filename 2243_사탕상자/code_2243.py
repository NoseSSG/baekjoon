# https://www.acmicpc.net/problem/2243
import sys
sys.stdin = open('input_2243.txt')
input = sys.stdin.readline
from math import ceil,log

def out_candy(s,e,idx,target):
    if s==e:
        return s
    mid = (s+e) // 2
    left_count = seg_tree[idx*2]
    if target <= left_count:
        return out_candy(s,mid,idx*2,target)
    else:
        return out_candy(mid+1,e,idx*2+1,target - left_count)

def add_candy(s,e,idx,target,cnt):
    if target < s or e < target:
        return
    seg_tree[idx] += cnt
    if s == e:
        return
    mid = (s+e)//2
    add_candy(s,mid,idx*2,target,cnt)
    add_candy(mid+1,e,idx*2+1,target,cnt)
    


N = int(input())
seg_tree = [0] * (4 * 1000000)


for _ in range(N):
    temp = list(map(int,input().split()))

    A = temp[0]
    if A == 1:
        # 사탕을 빼는 경우
        taste = out_candy(1,1000000,1,temp[1])
        print(taste)
        add_candy(1,1000000,1,taste,-1)
    else:
        # 사탕을 넣는 경우
        add_candy(1,1000000,1,temp[1],temp[2])
