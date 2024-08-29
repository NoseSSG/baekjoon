# https://www.acmicpc.net/problem/3085
import sys
sys.stdin = open('input_3085.txt','r')

def count_candy():
    cnt = 0
    for i in range(N):
        temp = 1
        for j in range(N-1):
            if candy[j][i] == candy[j + 1][i]:
                temp += 1
            else:
                cnt = max(cnt, temp)
                temp = 1
        cnt = max(cnt, temp)

    for i in range(N):
        temp = 1
        for j in range(N - 1):
            if candy[i][j] == candy[i][j + 1]:
                temp += 1
            else:
                cnt = max(cnt, temp)
                temp = 1
        cnt = max(cnt, temp)
    return cnt


T = 3


for test_case in range(1,T+1):
    N = int(input())
    candy = [list(map(str,input().rstrip())) for _ in range(N)]
    dx = [1,0]
    dy = [0,1]
    ans = 0
    for i in range(N):
        for j in range(N):
            for d in range(2):
                nx ,ny = i+dx[d] , j+dy[d]
                if nx < N and ny < N:
                    if candy[i][j] != candy[nx][ny]:
                        candy[i][j],candy[nx][ny] = candy[nx][ny],candy[i][j]
                        ans = max(ans,count_candy())
                        candy[i][j], candy[nx][ny] = candy[nx][ny], candy[i][j]

    print(f'#{test_case} {ans}')