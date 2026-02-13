# https://www.acmicpc.net/problem/1395
import sys
sys.stdin = open("input_1395.txt")
input = sys.stdin.readline

def push(s, e, idx):
    """idx 구간에 lazy(반전 예약)가 있으면 자식에게 내려보냄"""
    if lazy[idx] == 0 or s == e:
        return

    mid = (s + e) // 2
    left = idx *2
    right = idx * 2 + 1

    # 왼쪽 자식 [s, mid] 반전 적용
    tree[left] = (mid - s + 1) - tree[left]
    lazy[left] ^= 1

    # 오른쪽 자식 [mid+1, e] 반전 적용
    tree[right] = (e - (mid + 1) + 1) - tree[right]  # = (e - mid)
    lazy[right] ^= 1

    lazy[idx] = 0

def update(s, e, l, r, idx):
    """구간 [l, r] 반전"""
    if r < s or e < l:
        return

    if l <= s and e <= r:
        tree[idx] = (e - s + 1) - tree[idx]
        lazy[idx] ^= 1
        return

    push(s, e, idx)
    mid = (s + e) // 2
    update(s, mid, l, r, idx * 2)
    update(mid + 1, e, l, r, idx * 2 + 1)
    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]

def query(s, e, l, r, idx):
    """구간 [l, r] 켜진 스위치 개수"""
    if r < s or e < l:
        return 0

    if l <= s and e <= r:
        return tree[idx]

    push(s, e, idx)
    mid = (s + e) // 2
    return query(s, mid, l, r, idx * 2) + query(mid + 1, e, l, r, idx * 2 + 1)

N, M = map(int, input().split())
tree = [0] * (4 * N)
lazy = [0] * (4 * N)

out = []
for _ in range(M):
    o, s, t = map(int, input().split())
    if o == 0:
        update(1, N, s, t, 1)
    else:
        out.append(str(query(1, N, s, t, 1)))

print("\n".join(out))