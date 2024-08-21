import sys
sys.stdin = open('input_7453.txt','r')

N  = int(input())

arr = [ list(map(int,input().split())) for _ in range(N)]
rotate_arr = [[0]*N for _ in range(4)]
for i in range(N):
    for j in range(4):
        rotate_arr[j][N-i-1] = arr[i][j]