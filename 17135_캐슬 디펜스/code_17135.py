# https://www.acmicpc.net/problem/17135
import sys
# sys.stdin = open('input_17135.txt','r')

from itertools import permutations
from collections import deque

def BFS(a,turn,killed):
    d_que = deque()
    d_que.append((turn,a,0))

    while d_que:
        now_x,now_y,cnt = d_que.popleft()
        for d in range(3):
            next_x, next_y = now_x + dx[d], now_y + dy[d]
            if turn< next_x < N and 0 <= next_y < M and cnt<=D and (next_x,next_y) not in kill_enemy:
                if reverse_enemy[next_x][next_y]:
                    return (next_x,next_y)
                else:
                    d_que.append((next_x,next_y,cnt+1))





N,M,D = map(int,input().split())
enemy = [list(map(int,input().split())) for _ in range(N)]
reverse_enemy = enemy[::-1]

dx = [0,1,0]
dy = [-1,0,1]
ans = 0
temp = permutations(list(range(M)),3)
# for turn in range(-1,N-1):
#     temp_ans = 0
#     for i in temp:
#         kill_enemy = set()
#         for j in i:
#             kill = BFS(j,turn)
#             if kill is not None:
#                 kill_enemy.add(kill)
#         temp_ans = max(temp_ans,len(kill_enemy))
#     print(turn)
#     reverse_enemy[turn+1] = [0] * M
#     print(reverse_enemy)
#     ans += temp_ans
# print(ans)

for archers in temp:
    temp_ans = 0
    kill_enemy = set()
    for turn in range(-1,N-1):
        for archer in archers:
            kill = BFS(archer,turn,kill_enemy)
            if kill is not None:
                kill_enemy.add(kill)
    temp_ans = max(temp_ans,len(kill_enemy))
    ans = max(temp_ans,ans)
print(ans)