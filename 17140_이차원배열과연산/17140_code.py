# https://www.acmicpc.net/problem/17140
import sys
from queue import PriorityQueue
sys.stdin = open('input_17140.txt','r')

T = 7

def sort_r(arr_temp):
    # global y_len
    # y_len = 0
    weight = 0
    temp = []
    for line in arr_temp:
        d = {}
        p_que = PriorityQueue()
        for square in line:
            if square == 0 : continue
            if square in d: d[square] += 1
            else: d[square] = 1
        for key in d:
            p_que.put((d[key],key))
        temptemp = []
        while not p_que.empty():
            p_que_get = p_que.get()
            temptemp += [p_que_get[1],p_que_get[0]]
        if len(temptemp) > 100:
            temptemp = temptemp[:100]
        temp.append(temptemp)
        weight = max(weight,len(temptemp))
    height = len(temp)
    zero_base = [[0]*weight for _ in range(height)]
    for i in range(height):
        for j,v in enumerate(temp[i]):
            zero_base[i][j] = v

    return zero_base


def rotate_rever_clock(arr):
    height = len(arr)
    weight = len(arr[0])
    rotate_arr = [[0] * height for _ in range(weight)]
    for i in range(height):
        for j in range(weight):
            rotate_arr[weight-j-1][i] = arr[i][j]
    return rotate_arr

def rotate_clock(arr):
    height = len(arr)
    weight = len(arr[0])
    rotate_arr = [[0] * height for _ in range(weight)]
    for i in range(height):
        for j in range(weight):
            rotate_arr[j][height-i-1] = arr[i][j]
    return rotate_arr

def sort_c(arr):
    arr_temp = rotate_rever_clock(arr)
    arr_temp = sort_r(arr_temp)
    # global x_len
    # x_len = 0
    # weight = 0
    # temp = []
    # for line in arr_temp:
    #     d = {}
    #     p_que = PriorityQueue()
    #     for square in line:
    #         if square == 0: continue
    #         if square in d:
    #             d[square] += 1
    #         else:
    #             d[square] = 1
    #     for key in d:
    #         p_que.put((d[key], key))
    #     temptemp = []
    #     while not p_que.empty():
    #         p_que_get = p_que.get()
    #         temptemp += [p_que_get[1], p_que_get[0]]
    #     if len(temptemp) > 100:
    #         temptemp = temptemp[:100]
    #     temp.append(temptemp)
    #     weight = max(weight, len(temptemp))
    # height = len(temp)
    # zero_base = [[0] * weight for _ in range(height)]
    # for i in range(height):
    #     for j, v in enumerate(temp[i]):
    #         zero_base[i][j] = v

    arr_temp = rotate_clock(arr_temp)
    return arr_temp


for test_case in range(1,T+1):
    r,c,k = map(int,input().split())
    x_len, y_len = 3,3
    arr = [list(map(int,input().split())) for _ in range(x_len)]

    ans = -1
    for time in range(101):
        if r <= len(arr) and c <= len(arr[0]):
            if arr[r - 1][c - 1] == k:
                ans = time
                break
        if len(arr) >= len(arr[0]):
            arr = sort_r(arr)
        else:
            arr = sort_c(arr)
    print(ans)