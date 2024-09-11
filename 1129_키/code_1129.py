# https://www.acmicpc.net/problem/1129
import sys
# sys.stdin = open('input_1129.txt','r')


from collections import deque

N = int(input())
temp = list(map(int,input().split()))
temp.sort()
ans1 = []
ans2 = []
ans1.append(temp[0])
ans2.append(temp[0])
flag = 0
for i in temp[1:]:
    if i - ans1[-1]
    if flag == 0:
        ans1.append(i)
    else:
        ans2.append(i)

ans2.reverse()
ttt = ans1+ ans2[:-1]
d_que = deque(ttt)
min_ans = ttt
for _ in range(N):
    d_que.rotate(1)
    min_ans = min(min_ans,list(d_que))
print(*min_ans)