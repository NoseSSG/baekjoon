# https://www.acmicpc.net/problem/2042
import sys
sys.stdin = open('input_2042.txt','r')

def init(start,end,index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start+end) //2
    tree[index] = init(start,mid,index*2) + init(mid+1,end,index*2 +1)
    return tree[index]

def sum_tree(start,end,index,left,right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[index]
    mid = (start+end)//2
    return sum_tree(start,mid,index*2, left, right) + sum_tree(mid +1 ,end ,index*2+1, left, right)

def update(start,end,index,what,value):
    if what < start or what > end:
        return
    tree[index] += value
    if start == end:
        return
    mid = (start + end) //2
    update(start,mid,index*2,what,value)
    update(mid+1,end,index*2+1,what,value)



N,M,K = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

tree = [0] * (N*4)
init(0,N-1,1)

for _ in range(M+K):
    a,b,c =map(int,input().split())
    if a == 1:
        diff = c - arr[b-1]
        arr[b-1] = c
        update(0,N-1,1,b-1,diff)

    if a == 2:
        print(sum_tree(0,N-1,1,b-1,c-1))

