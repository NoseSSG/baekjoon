# https://www.acmicpc.net/problem/5676
import sys
sys.stdin = open('input_5676.txt')
input = sys.stdin.readline

def int2sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0

def make_seg(s,e,idx):
    if s==e:
        seg_tree[idx] = sign[s]
        return seg_tree[idx]
    mid = (s+e)//2
    seg_tree[idx] = make_seg(s,mid,idx*2) * make_seg(mid+1,e,idx*2+1)
    return seg_tree[idx]

def update(s,e,idx,target,diff):
    if target < s or e < target:
        return seg_tree[idx]
    if s == e:
        seg_tree[idx] = diff
        return seg_tree[idx]
    mid = (s+e)//2
    left = update(s,mid,idx*2,target,diff)
    right = update(mid+1,e,idx*2+1,target,diff)
    seg_tree[idx] = left * right
    return seg_tree[idx]


def query(s,e,l,r,idx):
    if r <s or e < l:
        return 1
    if l <= s and e <= r:
        return seg_tree[idx]
    mid = (s+e)//2
    return query(s,mid,l,r,idx*2) * query(mid+1,e,l,r,idx*2+1)

while True:
    try:
        line = input().split()
        if not line:
            break
        N,K = map(int,line)
        temp = list(map(int,input().split()))
        sign = [0] * (N+1)
        seg_tree = [0] * (4 * N)

        for i in range(1,N+1):
            sign[i] = int2sign(temp[i-1])

        make_seg(1,N,1)

        answer = []

        for _ in range(K):
            a,b,c = map(str,input().split())
            b,c = int(b),int(c)
            
            if a == "C":
                # 변경
                update(1,N,1,b,int2sign(c))

            if a =="P":
                # 곱셈
                ans = query(1,N,b,c,1)
                if ans > 0:
                    answer.append('+')
                elif ans < 0 :
                    answer.append('-')
                else:
                    answer.append('0')
        print(''.join(answer))
            
    except EOFError:
        break

