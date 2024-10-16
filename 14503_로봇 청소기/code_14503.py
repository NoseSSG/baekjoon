# https://www.acmicpc.net/problem/14503
import sys
# sys.stdin = open('input_14503.txt','r')

def can_i_turn(x,y,dir):
    for _ in range(4):
        dir -=1
        if dir <0: dir = 3
        nx, ny = x + dx[dir], y + dy[dir]
        if room[nx][ny] == 0:
            return dir
    return -1

def can_i_back(x,y,dir):
    dir = (dir+2)%4
    nx, ny = x + dx[dir], y + dy[dir]
    if room[nx][ny] == 1:
        return False
    return True



N,M = map(int,input().split())
robot_x, robot_y , robot_dir = map(int,input().split())

room = [list(map(int,input().split())) for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0
while True:
    if room[robot_x][robot_y] == 0:
        cnt += 1
        room[robot_x][robot_y] = 2

    new_dir = can_i_turn(robot_x,robot_y,robot_dir)
    if new_dir == -1:
        if can_i_back(robot_x,robot_y,robot_dir):
            new_dir = (robot_dir+2)%4
            robot_x, robot_y = robot_x + dx[new_dir], robot_y + dy[new_dir]
        else:
            break
    else:
        robot_dir = new_dir
        robot_x,robot_y = robot_x+dx[robot_dir],robot_y+dy[robot_dir]

print(cnt)
