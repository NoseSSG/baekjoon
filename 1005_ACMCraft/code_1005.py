# https://www.acmicpc.net/problem/1005
import sys
# sys.stdin = open('input_1005.txt','r')

T = int(input())

def DFS(start):
    if start in DP: return DP[start]

    if not parent_node[start]:
        return time[start-1]

    how_time = 0
    for i in parent_node[start]:
        temp_time = DFS(i)
        if how_time < temp_time: how_time=temp_time
    DP[start] = how_time + time[start-1]

    return DP[start]

for test_case in range(1,T+1):
    N,K = map(int,sys.stdin.readline().split())
    time = list(map(int,sys.stdin.readline().split()))
    parent_node = {}
    for i in range(N+1):
        parent_node[i] = []
    for _ in range(K):
        a,b = map(int,sys.stdin.readline().split())
        parent_node[b].append(a)

    target_idx = int(input())
    # DP = [0] * (N+1)
    # DP를 미리 배열로 선언시 시간초과 발생
    DP = {}
    print(DFS(target_idx))