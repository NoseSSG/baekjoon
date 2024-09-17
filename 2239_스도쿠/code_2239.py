# https://www.acmicpc.net/problem/2239
import sys
sys.stdin = open('input_2239.txt','r')

def check_row(num,idx):
    for i in sudoku[idx]:
        if i == num:
            return False
    return True

def check_cal(num,idx):
    for i in range(9):
        if num == sudoku[i][idx]:
            return False
    return True

def check_box(num,x,y):
    find_x = x//3
    find_y = y//3
    for i in range(3*find_x,3*find_x+3):
        for j in range(3*find_y,3*find_y+3):
            if sudoku[i][j] == num:
                return False
    return True

def fill_sudoku(start):
    if start == 81:
        for i in sudoku:
            print(*i,sep='')
        exit()
    x = start // 9
    y = start % 9
    if sudoku[x][y] != 0:
        fill_sudoku(start+1)
    else:
        for num in range(1,10):
            if check_cal(num,y) and check_row(num,x) and check_box(num,x,y):
                sudoku[x][y] = num
                fill_sudoku(start+1)
                sudoku[x][y] = 0

sudoku = [list(map(int,input())) for _ in range(9)]
fill_sudoku(0)