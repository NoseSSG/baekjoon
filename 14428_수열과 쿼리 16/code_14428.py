# https://www.acmicpc.net/problem/14428
import sys
import math

sys.stdin = open('input_14428.txt')

def make_seg(left,right,index):
    if left == right:
        tree[index] = [temp[left],left+1]
        return tree[index]
    
    mid = (left+right) //2
    tree[index] = min(make_seg(left,mid,index*2),make_seg(mid+1,right,index*2+1))
    return tree[index]

def update_tree(start,end,index,target,num):
    if start > target or end < target:
        return tree[index]
    if start == end:
        tree[index] = [num,target+1]
        return tree[index]
    
    mid = (start+end) // 2
    left_result = update_tree(start,mid,index*2,target,num)
    right_result = update_tree(mid+1,end,index*2+1,target,num)
    # print(left_result,right_result,end='!!!!!!!!!!!\n')
    # tree[index] = min(update_tree(start,mid,index*2,target,num),update_tree(mid+1,end,index*2+1,target,num))
    tree[index] = min(left_result,right_result)
    return tree[index]


def find_min(start,end,index,left,right):
    if start > right or end < left:
        return [float('inf'),float('inf')]
    if left <= start and end <= right:
        return tree[index]
    
    mid = (start+end)//2
   
    return min(find_min(start,mid,index*2,left,right),find_min(mid+1,end,index*2+1,left,right))


N = int(input())
temp = list(map(int,input().split()))
tree = [0] * 2 ** (math.ceil(math.log(N,2)+1))

make_seg(0,N-1,1)

M = int(input())

for _ in range(M):
    order,i,j = map(int,input().split())
    if order == 1:
        update_tree(0,N-1,1,i-1,j)
        # print(tree)
    else:
        result =  find_min(0,N-1,1,i-1,j-1)
        print(result[1])