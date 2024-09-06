# https://www.acmicpc.net/problem/14712
import sys
sys.stdin = open('input_14712.txt','r')

def Brute_force(x,y):
    # 이전 값을 확인해야함 어떻게?
    # 지나온 옆 위 왼쪽위 들을 확인해서 지나감
    # nemo를 테두리를 만들어서 위/ 왼쪽도 고려
    global ans
    if x == N+1:
        ans += 1
        return
    if y == M:
        nx = x + 1
        ny = 1
    else:
        nx = x
        ny = y+1
    if nemo[x-1][y] == 0 or nemo[x][y-1] == 0 or nemo[x-1][y-1] == 0:
        nemo[x][y] = 1
        Brute_force(nx,ny)
        nemo[x][y] = 0
    Brute_force(nx,ny)

N,M = map(int,input().split())
nemo = [[0]*(M+1) for _ in range(N+1)]
ans = 0
Brute_force(1,1)
print(ans)