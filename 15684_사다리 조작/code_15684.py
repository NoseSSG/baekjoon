# https://www.acmicpc.net/problem/15684
import sys
import pprint
# sys.stdin = open('input_15684.txt','r')

T = 3

def check_ladder():
    for i in range(N):
        idx = i
        depth = 0
        for _ in range(H):
            if ladder[depth][idx] != 0:
                idx += ladder[depth][idx]
            depth += 1
        if i != idx: return False
    return True

def DFS(cnt,x):
    if check_ladder():
        return cnt
    if cnt >= 3:
        return -1
    t = -1
    for i in range(x,N-1):
        for j in range(H):
            if ladder[j][i] == 0 and ladder[j][i+1] == 0:
                ladder[j][i] = 1
                ladder[j][i+1] = -1
                temp = DFS(cnt+1,i)
                if t == -1: t = temp
                elif temp != -1 : t = min(t,temp)
                ladder[j][i] = 0
                ladder[j][i+1] = 0
    return t


# for test_case in range(1,T+1):
N, M, H = map(int,input().split())
ladder = [[0]*N for _ in range(H)]
for _ in range(M):
    x,y = map(int,input().split())
    ladder[x-1][y-1] = 1
    ladder[x-1][y] = -1

print(DFS(0,0))