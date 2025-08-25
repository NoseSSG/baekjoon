# https://www.acmicpc.net/problem/5639
import sys
sys.stdin = open('input_5639.txt','r')

temp = []

while(True):
    try:
        temp.append(int(input()))
    except:
        break

def solution(A):
    if len(A) == 0:
        return
    mid = A[0]
    temp_left = []
    temp_right = []
    temp_left = A[1:]
    for i in range(1,len(A)):
        if A[i] > mid:
            temp_left = A[1:i]
            temp_right = A[i:]
            break
    solution(temp_left)
    solution(temp_right)
    print(mid)
solution(temp)
