# https://www.acmicpc.net/problem/13537
import sys
sys.stdin = open('input_13537.txt')
input = sys.stdin.readline
from bisect import bisect_right

def make_seg(s,e,idx):
    if s == e :
        seg_tree[idx] = [temp[s]]
        return seg_tree[idx]
    
    mid = (s + e) // 2
    left = make_seg(s,mid,idx*2)
    right = make_seg(mid+1,e,idx*2+1)

    seg_tree[idx] = sorted(left + right)
    return seg_tree[idx]


def query(s,e,l,r,idx,k):
    if r < s or e < l:
        return 0
    if l <= s and e <=r:
        t = seg_tree[idx]
        return len(t) - bisect_right(t,k)
    mid = (s+e)//2
    return query(s,mid,l,r,idx*2,k) + query(mid+1,e,l,r,idx*2+1,k)

N = int(input())
temp = [0] + list(map(int,input().split()))
M = int(input())
seg_tree = [0] * (4 * N)

make_seg(1,N,1)

for _ in range(M):
    i,j,k = map(int,input().split())
    print(query(1,N,i,j,1,k))
