# https://www.acmicpc.net/problem/8896
import sys
sys.stdin = open('input_8896.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    robot = [list(input().rstrip()) for _ in range(N)]
    survive = set(range(N))
    # print(survive)
    for i in range(len(robot[0])):
        result = {'R':[],'S':[],'P':[]}
        for what_robot in survive:
            result[robot[what_robot][i]].append(what_robot)

        if not result['R'] and result['S']:
            for idx in result['P']:
                survive.discard(idx)
        elif not result['S'] and result['P']:
            for idx in result['R']:
                survive.discard(idx)
        elif not result['P'] and result['R']:
            for idx in result['S']:
                survive.discard(idx)
        else:
            continue
        if len(survive) == 1:
            for i in survive:
                print(i+1)
            break
    if len(survive) > 1:
        print(0)