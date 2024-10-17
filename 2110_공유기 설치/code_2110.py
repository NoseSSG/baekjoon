# https://www.acmicpc.net/problem/2110
import sys
sys.stdin = open('input_2110.txt')

N,C = map(int,input().split())
home = [int(input()) for _ in range(N)]
home.sort()
start = 1
end = home[-1] - home[0]
while start <= end:
    mid = (start+end)//2
    cnt = 1
    now = home[0]
    for i in range(1,N):
        if home[i] >= now + mid:
            cnt += 1
            now = home[i]
    if cnt >= C:
        start = mid +1
    else:
        end = mid - 1

print(end)
