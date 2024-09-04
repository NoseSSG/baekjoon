# https://www.acmicpc.net/problem/23309
import sys
# sys.stdin = open('input_23309.txt','r')

input = sys.stdin.readline
N,M = map(int,input().split())
num = list(map(int,input().split()))
before_station = [0] * 1000001
next_station = [0] * 1000001
for i in range(N):
    next_station[num[i-1]] = num[i]
    before_station[num[i]] = num[i-1]
for _ in range(M):
    text = list(map(str,input().split()))
    order = text[0]
    if order == 'BN':
        now_station = int(text[1])
        new_station =  int(text[2])
        next_ = next_station[now_station]
        next_station[now_station] = new_station
        next_station[new_station] = next_
        before_station[next_] = new_station
        before_station[new_station] = now_station
        print(next_)
    elif order == 'BP':
        now_station = int(text[1])
        new_station =  int(text[2])
        before_ = before_station[now_station]
        before_station[now_station] = new_station
        before_station[new_station] = before_
        next_station[before_] = new_station
        next_station[new_station] = now_station
        print(before_)

    elif order == 'CN':
        now_station = int(text[1])
        next_ = next_station[now_station]
        next_next_ = next_station[next_]
        next_station[now_station] = next_next_
        before_station[next_next_] = now_station
        print(next_)
        before_station[next_] = 0
        next_station[next_] = 0

    elif order == 'CP':
        now_station = int(text[1])
        before_ = before_station[now_station]
        before_before_ = before_station[before_]
        before_station[now_station] = before_before_
        next_station[before_before_] = now_station
        print(before_)
        before_station[before_] = 0
        next_station[before_] = 0

# input = sys.stdin.readline
# N,M = map(int,input().split())
# num = list(map(int,input().split()))
# line = {}
# for i in range(N):
#     if i==N-1:
#         line[num[i]] = [num[i-1],num[0]]
#         continue
#     line[num[i]] = [num[i-1],num[i+1]]
#
# for _ in range(M):
#     text = list(map(str,input().split()))
#
#     order = text[0]
#     if order == 'BN':
#         now_station = int(text[1])
#         new_station = int(text[2])
#         right_station = line[now_station][1]
#         line[now_station][1] = new_station
#         line[right_station][0] = new_station
#         line[new_station] = [now_station,right_station]
#         print(right_station)
#     elif order == 'BP':
#         now_station = int(text[1])
#         new_station = int(text[2])
#         left_station = line[now_station][0]
#         line[now_station][0] = new_station
#         line[left_station][1] = new_station
#         line[new_station] = [left_station,now_station]
#         print(left_station)
#     elif order == 'CN':
#         now_station = int(text[1])
#         right_station = line[now_station][1]
#         right_right_station = line[right_station][1]
#         line[now_station][1] = right_right_station
#         line[right_right_station][0] = now_station
#         print(right_station)
#         line.pop(right_station)
#
#     elif order == 'CP':
#         now_station = int(text[1])
#         left_station = line[now_station][0]
#         left_left_station = line[left_station][0]
#         line[now_station][0] = left_left_station
#         line[left_left_station][1] = now_station
#         print(left_station)
#         line.pop(left_station)

