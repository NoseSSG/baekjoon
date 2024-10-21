# https://www.acmicpc.net/problem/2138
import sys

sys.stdin = open('input_2138.txt','r')

def press_btn(A,B):
    A_copy = A[:]
    cnt = 0
    for i in range(1,len(A)):
        if A_copy[i-1] == B[i-1]:
            continue
        for l in range(-1,2,1):
            next_idx = i + l
            if 0<=next_idx<len(A):
                A_copy[next_idx] = (A_copy[next_idx]+1) % 2
        cnt+=1

    if A_copy == B:
        return cnt
    else:
        return float('inf')


N = int(input())
status = list(map(int,input()))
goal = list(map(int,input()))
temp = press_btn(status,goal)
status[0] = (status[0]+1) % 2
status[1] = (status[1]+1) % 2

ans = min(temp,press_btn(status,goal)+1)

if ans == float('inf'): ans = -1
print(ans)