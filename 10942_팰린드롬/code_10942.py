# https://www.acmicpc.net/problem/10942
import sys
sys.stdin = open('input_10942.txt','r')
input = sys.stdin.readline

N = int(input())
num = list(map(int,input().split()))
DP = [[0] * N for _ in range(N)]
M = int(input())

for i in range(N):
    for j in range(N-i):
        end = j + i
        if j == end:
            DP[j][end] = 1
        elif num[j] == num[end]:
            if j + 1 == end:
                DP[j][end] = 1
            elif DP[j+1][end-1] == 1:
                DP[j][end] = 1

for _ in range(M):
    a,b = map(int,input().split())
    print(DP[a-1][b-1])