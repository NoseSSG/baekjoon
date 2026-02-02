# https://www.acmicpc.net/problem/23631
import sys
sys.stdin = open('input_23631.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N,K = map(int,input().split())

    distance = lambda i:(i*(i+1)*K) // 2
    left = 0
    right = N-1
    while left < right:
        mid = (left+right)//2
        if distance(mid) > N-1 : right = mid
        else: left = mid + 1
    
    cnt = left -1
    dist = distance(cnt)
    if cnt % 2 == 1:
        dir = "L"
        pos = (cnt // 2 + 1) * K -(N-1-dist)
    else:
        dir = "R"
        pos = -(cnt//2) * K + (N-1-dist)

    print(pos,dir)