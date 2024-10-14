# https://www.acmicpc.net/problem/17144
import sys
from tkinter.ttk import Label

sys.stdin = open('input_17144.txt','r')

def spread_dust(room):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    after_room = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if room[i][j] == -1 or room[i][j] == 0 or room[i][j] < 5:
                after_room[i][j] += room[i][j]
                continue
            count = 0
            for d in range(4):
                nx,ny = i + dx[d] , j + dy[d]
                if 0 <= nx < R and 0 <= ny < C:
                    if room[nx][ny] == -1:
                        continue
                    after_room[nx][ny] += room[i][j]//5
                    count += 1
            after_room[i][j] += room[i][j] - (room[i][j]//5)*count
    return after_room


R,C,T = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(R)]
room = spread_dust(room)
room = spread_dust(room)
for i in room:
    print(*i)
