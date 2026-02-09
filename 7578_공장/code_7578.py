# https://www.acmicpc.net/problem/7578
import sys
sys.stdin = open('input_7578.txt')
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

seg_tree = [0] * (4 * N)

pos = {}
for i,a in enumerate(B):
    pos[a] = i

ans = 0

def update(s,e,idx,target,diff):
    if target < s or e < target:
        return
    seg_tree[idx] += diff
    if s==e:
        return
    mid = (s+e)//2
    update(s,mid,idx*2,target,diff)
    update(mid+1,e,idx*2+1,target,diff)

def query(s,e,idx,l,r):
    if r < s or e < l:
        return 0
    if l <= s and e <= r:
        return seg_tree[idx]
    mid = (s+e)//2
    return query(s,mid,idx*2,l,r) + query(mid+1,e,idx*2+1,l,r)
    


for x in A:
    p = pos[x]
    if p < N:
        ans += query(1,N,1,p+1,N)
    update(1,N,1,p,1)

print(ans)