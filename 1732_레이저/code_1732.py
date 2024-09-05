# https://www.acmicpc.net/problem/1732
import sys
sys.stdin = open('input_1732.txt','r')

from decimal import Decimal
N = int(input())
degree = {}
ans = set()
flag = False
for _ in range(N):
    x,y,d = map(int,input().split())
    if x == 0 and y == 0:
        flag = True
        continue

    if x == 0: deg = 'x_zero'
    elif y==0:
        if x >0: deg = 'plus_zero'
        else: deg = 'minus_zero'
    else: deg = y/x

    if deg not in degree:
        degree[deg] = []
    degree[deg].append([abs(x)+abs(y),x,y,d])


if flag:
    for value in degree.values():
        for temp in value:
            ans.add((temp[1],temp[2]))
else:
    for value in degree.values():
        if len(value) == 1: continue
        arr = value
        arr.sort()
        max_height = -1
        for temp in arr:
            if max_height < temp[3]:
                max_height = temp[3]
            else:
                ans.add((temp[1],temp[2]))

answer = list(ans)
answer.sort()
print(degree)
for i in answer:
    print(i[0],i[1])
# degree = {1:{},2:{},3:{},4:{}}
# for _ in range(N):
#     x,y,d = map(int,input().split())
#     if x == 0: deg = 0
#     else: deg = y/x
#     if x >= 0 and y >= 0:
#         if deg not in degree[1]:
#             degree[1][deg] = []
#         degree[1][deg].append([abs(x)+abs(y),x,y,d])
#     elif x < 0 <= y:
#         if deg not in degree[2]:
#             degree[2][deg] = []
#         degree[2][deg].append([abs(x)+abs(y),x,y,d])
#     elif x < 0 and y < 0:
#         if deg not in degree[3]:
#             degree[3][deg] = []
#         degree[3][deg].append([abs(x)+abs(y),x,y,d])
#     else:
#         if deg not in degree[4]:
#             degree[4][deg] = []
#         degree[4][deg].append([abs(x)+abs(y),x,y,d])
#
# for key in degree:
#     print(degree[key])
#     for value in degree[key]:
#         if len(degree[key][value]) == 1: continue
#         max_height = 0
#         buildings = degree[key][value]
#         buildings.sort()
#         for building in buildings:
#             if building[3] > max_height:
#                 max_height = building[3]
#             else:
#                 ans.add((building[1],building[2]))
# answer = list(ans)
# answer.sort()
#
# for i in answer:
#     print(*i)