# https://www.acmicpc.net/problem/15654
import sys
# sys.stdin = open('input_15654.txt','r')

def DFS(select,not_select):
    if len(select)==M:
        print(*select)
        return
    for idx in range(len(not_select)):
        DFS(select +[not_select[idx]],not_select[:idx]+not_select[idx+1:])

N,M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
DFS([],num)