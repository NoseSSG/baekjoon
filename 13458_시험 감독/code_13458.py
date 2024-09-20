# https://www.acmicpc.net/problem/13458
import sys
# sys.stdin = open('input_13458.txt','r')
#
N = int(input())
temp = list(map(int,input().split()))
a,b =map(int,input().split())
ans = 0
for now in temp:
    if now <= a:
        ans+=1
    else:
        now -= a
        ans += 1
        if now % b: ans += 1
        ans += now//b
print(ans)