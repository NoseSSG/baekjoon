# https://www.acmicpc.net/problem/11066
import sys
sys.stdin = open('input_11066.txt')

test_case = int(input())

for _ in range(test_case):
    M = int(input())
    pages = [0] + list(map(int,input().split()))
    DP = [[0]*(M+1) for _ in range(M+1)]
    for i in range(M):
        DP[i][i+1] = pages[i] + pages[i+1]
    
    for i in range(M-1,0,-1):
        for j in range(M+1):
            if DP[i][j]==0 and j>i:
                DP[i][j] = min(DP[i][k] + DP[k+1][j] for k in range(i,j)) + sum(pages[i:j+1])

    print(DP[1][M])
