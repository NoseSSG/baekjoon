# https://www.acmicpc.net/problem/1406
import sys
sys.stdin = open('input_1406.txt','r')

T = 3
for test_case in range(1,T+1):
    L_cursor = list(map(str,input().rstrip()))
    R_cursor = []
    N = int(input())
    for _ in range(N):
        order = list(map(str,input().split()))
        if order[0] == 'L':
            if L_cursor:
                R_cursor.append(L_cursor.pop())
        elif order[0] == 'D':
            if R_cursor:
                L_cursor.append(R_cursor.pop())
        elif order[0] == 'B':
            if L_cursor: L_cursor.pop()
        elif order[0] == 'P':
            L_cursor.append(order[1])
    ans = ''.join(L_cursor+R_cursor[::-1])
    print(f'#{test_case} {ans}')
