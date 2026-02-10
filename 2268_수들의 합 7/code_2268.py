# https://www.acmicpc.net/problem/2268
import sys
sys.stdin = open("input_2268.txt")
input = sys.stdin.readline

def update(s,e,idx,target,diff):
    if target < s or e < target:
        return
    seg_tree[idx] += diff
    if s==e:
        return
    mid = (s+e)//2
    update(s,mid,idx*2,target,diff)
    update(mid+1,e,idx*2+1,target,diff)

def query(s,e,l,r,idx):
    if r < s or e < l:
        return 0
    if l<=s and e<=r:
        return seg_tree[idx]
    mid = (s+e)//2
    return query(s,mid,l,r,idx*2) + query(mid+1,e,l,r,idx*2+1)


N,M = map(int,input().split())
temp = [0] * (N+1)
seg_tree = [0] * (4 * N)

for _ in range(M):
    A,B,C = map(int,input().split())

    if A == 0:
        if B>C:
            B,C = C,B
        print(query(1,N,B,C,1))
    else:
        update(1,N,1,B,C-temp[B])
        temp[B]=C