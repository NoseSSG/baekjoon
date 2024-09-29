# https://www.acmicpc.net/problem/18111
import sys
# sys.stdin = open('input_18111.txt','r')

N,M,B = map(int,input().split())
mine_map = []
for _ in range(N):
    temp = map(int,input().split())
    mine_map += temp
high = max(mine_map)
low = min(mine_map)
timer = float('inf')
setup_height = 0
for height in range(low,high+1):
    now_time = 0
    need_block = 0
    for now in mine_map:
        if now < height:
            need_block += height - now
        else:
            now_time += (now - height)
    if now_time + B < need_block:
        continue
    now_time *= 2
    now_time += need_block
    if timer >= now_time:
        timer = now_time
        setup_height = height

print(timer,setup_height)