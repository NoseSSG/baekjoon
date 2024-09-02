# https://www.acmicpc.net/problem/1732
import sys
sys.stdin = open('input_1732.txt','r')

N = int(input())
degree = {}
ans = set()
for _ in range(N):
    x,y,d = map(int,input().split())
    deg = y/x

    if deg not in degree:
        degree[deg] = {d:(x,y)}
    else:
        if d not in degree[deg]:
            degree[deg][d] = (x,y)
        else:
            if abs(sum(degree[deg][d])) > abs(x+y):
                ans.add(degree[deg][d])
            else:
                ans.add((x,y))
answer = list(ans)
answer.sort()
for i in answer:
    print(*i)


