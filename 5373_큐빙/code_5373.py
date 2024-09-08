# https://www.acmicpc.net/problem/5373
import sys
sys.stdin = open('input_5373.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    order = list(map(str,input().split()))
    color = ['w', 'r', 'y', 'o', 'g', 'b']
    cube = []
    for c in color:
        temp = [[c] * 3 for _ in range(3)]
        cube.append(temp)
    for o in order:
        if o[0] == 'L':
            if o[1] =='+':
                for i in range(3):
                    cube[0][i][0],cube[1][i][0],cube[2][i][0],cube[3][2-i][0] = cube[3][2-i][0],cube[0][i][0],cube[1][i][0],cube[2][i][0]
                cube[4] = list(map(list,zip(*cube[4][::-1])))
            elif o[1] == '-':
                for i in range(3):
                    cube[0][i][0],cube[1][i][0],cube[2][i][0],cube[3][2-i][0] = cube[1][i][0],cube[2][i][0],cube[3][2-i][0],cube[0][i][0]
                cube[4] = list(map(list, zip(*cube[4])))[::-1]
        elif o[0] == 'R':
            if o[1] == '+':
                for i in range(3):
                    cube[0][i][2], cube[1][i][2], cube[2][i][2], cube[3][2-i][2] = cube[1][i][2], cube[2][i][2], cube[3][2-i][2],cube[0][i][2]
                cube[5] = list(map(list, zip(*cube[5][::-1])))
            elif o[1] == '-':
                for i in range(3):
                    cube[0][i][2], cube[1][i][2], cube[2][i][2], cube[3][2-i][2] = cube[3][2-i][2],cube[0][i][2], cube[1][i][2], cube[2][i][2]
                cube[5] = list(map(list, zip(*cube[5])))[::-1]
        elif o[0] == 'U':
            if o[1] == '+':
                for i in range(3):
                    cube[5][0][i],cube[3][0][2-i],cube[4][0][i],cube[1][0][i] = cube[3][0][2-i],cube[4][0][i],cube[1][0][i],cube[5][0][i]
                cube[0] = list(map(list,zip(*cube[0][::-1])))
            elif o[1] == '-':
                for i in range(3):
                    cube[5][0][i], cube[3][0][2-i], cube[4][0][i], cube[1][0][i] = cube[1][0][i],cube[5][0][i],cube[3][0][2-i], cube[4][0][i],
                cube[0] = list(map(list,zip(*cube[0])))[::-1]
        elif o[0] == 'D':
            if o[1] == '+':
                for i in range(3):
                    cube[5][2][i], cube[3][2][2-i], cube[4][2][i], cube[1][2][i] = cube[1][2][i], cube[5][2][i], \
                                                                                 cube[3][2][2-i], cube[4][2][i],
                cube[2] = list(map(list, zip(*cube[2][::-1])))
            elif o[1] == '-':
                for i in range(3):
                    cube[5][2][i], cube[3][2][2-i], cube[4][2][i], cube[1][2][i] = cube[3][2][2-i], cube[4][2][i], \
                                                                                 cube[1][2][i], cube[5][2][i]
                cube[2] = list(map(list, zip(*cube[2])))[::-1]

        elif o[0] == 'F':
            if o[1] == '+':
                for i in range(3):
                    cube[0][2][i],cube[5][i][0],cube[2][0][2-i],cube[4][2-i][2] = cube[4][2-i][2],cube[0][2][i],cube[5][i][0],cube[2][0][2-i]
                cube[1] = list(map(list, zip(*cube[1][::-1])))
            elif o[1] == '-':
                for i in range(3):
                    cube[0][2][i],cube[5][i][0],cube[2][0][2-i],cube[4][2-i][2] = cube[5][i][0],cube[2][0][2-i],cube[4][2-i][2],cube[0][2][i]
                cube[1] = list(map(list, zip(*cube[1])))[::-1]
        elif o[0] == 'B':
            if o[1] == '+':
                for i in range(3):
                    cube[0][0][i], cube[5][i][2],cube[2][2][2-i],cube[4][2-i][0] = cube[5][i][2],cube[2][2][2-i],cube[4][2-i][0],cube[0][0][i]
                cube[3] = list(map(list, zip(*cube[3])))[::-1]
            elif o[1] == '-':
                for i in range(3):
                    cube[0][0][i], cube[5][i][2],cube[2][2][2-i],cube[4][2-i][0] = cube[4][2-i][0],cube[0][0][i], cube[5][i][2],cube[2][2][2-i]
                cube[3] = list(map(list, zip(*cube[3][::-1])))
        # for c in cube:
        #     for t in c:
        #         print(*t)
        #     print()
        # print('-------------')
    for t in cube[0]:
        print(*t,sep='')
