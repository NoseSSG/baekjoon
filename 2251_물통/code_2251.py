# https://www.acmicpc.net/problem/2251
import sys
sys.stdin = open('input_2251.txt','r')

from collections import deque

def check_water(a,b,c):
    if (a,b,c) in check: return
    check.add((a,b,c))
    d_que.append((a,b,c))


def move_water(a,b,c):
    # 첫번째 컵 -> 두번째 컵
    water = min(a,cups[1]-b)
    check_water(a-water,b+water,c)

    # 첫번째 컵 -> 세번째 컵
    water = min(a,cups[2]-c)
    check_water(a-water,b,c+water)

    # 두번째 컵 -> 첫번째 컵
    water = min(b,cups[0]-a)
    check_water(a+water, b-water, c)

    # 두번째 컵 -> 세번째 컵
    water = min(b,cups[2]-c)
    check_water(a, b-water, c+water)

    # 세번째 컵 -> 첫번째 컵
    water = min(c,cups[0]-a)
    check_water(a+water, b, c-water)

    # 세번째 컵 -> 두번째 컵
    water = min(c,cups[1]-b)
    check_water(a, b+water, c-water)


cups = {i: x for i, x in enumerate(map(int, input().split()))}

check = set()
d_que = deque()
d_que.append((0,0,cups[2]))
ans = set()

while d_que:
    x,y,z = d_que.popleft()
    if x == 0:
        ans.add(z)
    move_water(x,y,z)

ans = list(ans)
ans.sort()
print(*ans)