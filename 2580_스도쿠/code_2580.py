# https://www.acmicpc.net/problem/2580
import sys
sys.stdin = open('input_2580.txt','r')

def print_sudoku():
    for i in sudoku:
        print(*i)


def check_row(x,num):
    for i in range(9):
        if sudoku[x][i] == num:
            return False
    return True

def check_column(y,num):
    for i in range(9):
        if sudoku[i][y] == num:
            return False
    return True

def check_box(x,y,num):
    x_i = (x//3)*3
    y_i = (y//3)*3

    for i in range(3):
        for j in range(3):
            if sudoku[x_i+i][y_i+j]==num:
                return False
    return True


def fill_sudoku(start):

    if start==81:
        print_sudoku()
        exit()

    x = start // 9
    y = start % 9
    if sudoku[x][y] == 0:
        for i in range(1,10):
            if check_row(x,i) and check_column(y,i) and check_box(x,y,i):
                sudoku[x][y] = i
                fill_sudoku(start+1)
                sudoku[x][y] = 0
        if sudoku[x][y]==0:
            return
    else:
        fill_sudoku(start+1)
sudoku = [list(map(int,input().split())) for _ in range(9)]
fill_sudoku(0)