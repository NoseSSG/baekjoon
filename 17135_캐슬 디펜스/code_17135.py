# https://www.acmicpc.net/problem/17135
import sys
# sys.stdin = open('input_17135.txt','r')

from itertools import combinations
from collections import deque

def BFS(archers):
    copy_enemy = [row[:] for row in enemy]
    total_kills = 0

    for i in range(N-1, -1, -1):
        killed_enemy = set()
        for archer in archers:
            d_que = deque([(i, archer, 1)])  # (x, y, cnt)
            while d_que:
                x, y, cnt = d_que.popleft()
                if cnt > D:
                    break
                if copy_enemy[x][y] == 1:
                    killed_enemy.add((x, y))
                    break

                for d in range(3):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < N and 0 <= ny < M:
                        d_que.append((nx, ny, cnt + 1))

        for x, y in killed_enemy:
            if copy_enemy[x][y] == 1:
                total_kills += 1
                copy_enemy[x][y] = 0

    return total_kills

N, M, D = map(int, input().split())
enemy = [list(map(int, input().split())) for _ in range(N)]
dx = [0, -1, 0]
dy = [-1, 0, 1]

ans = 0
for archers in combinations(range(M), 3):
    ans = max(ans, BFS(archers))

print(ans)
