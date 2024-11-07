# https://www.acmicpc.net/problem/1700
import sys
# sys.stdin = open('input_1700.txt')

def find_latest(i):
    num = 0
    last_idx = -1
    for plug in plugs:
        try:
            plug_idx = temp[i:].index(plug)
        except:
            return plug
        if last_idx < plug_idx:
            last_idx,num = plug_idx,plug
    return num



N,M = map(int,input().split())
temp = list(map(int,input().split()))

plugs = set()
ans = 0
for idx,value in enumerate(temp):
    plugs.add(value)
    if len(plugs) > N:
        ans += 1
        take_off = find_latest(idx)
        plugs.discard(take_off)
print(ans)