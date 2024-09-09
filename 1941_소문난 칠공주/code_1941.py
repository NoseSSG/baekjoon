# https://www.acmicpc.net/problem/1941
import sys
sys.stdin = open('input_1941.txt','r')

from collections import deque

def DFS(x,y):
    temp = deque()
    temp.append([(x,y)])
    while temp:
        now = temp.popleft()
        # print(now)
        if len(now) == 7:
            cnt = 0
            for i in now:
                if member[i[0]][i[1]] == 'S':
                    cnt += 1
            if cnt >=4:
                now.sort()
                visited.add(tuple(now))
            continue
        for x,y in now:
            for d in range(4):
                nx, ny =x+dx[d] , y+dy[d]
                if (nx,ny) not in now and 0<= nx < 5 and 0<= ny < 5:
                    temp.append(now+[(nx,ny)])

member = [list(map(str,input().rstrip())) for _ in range(5)]
visited = set()
ans = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for i in range(5):
    for j in range(5):
        if member[i][j] == 'S':
            DFS(i,j)
print(len(visited))