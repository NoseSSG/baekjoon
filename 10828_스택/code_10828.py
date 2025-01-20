# https://www.acmicpc.net/problem/10828
import sys
sys.stdin = open('input_10828.txt')

N = int(input())

stack = []
size = 0

for _ in range(N):
    temp = list(map(str,input().split()))
    
    order = temp[0]
    if order == 'push':
        stack.append(temp[1])
        size += 1
    elif order == 'pop':
        if size == 0:
            print(-1)
        else:
            print(stack.pop())
            size -= 1
    elif order == 'size':
        print(size)
    elif order == 'empty':
        if size == 0:
            print(1)
        else:
            print(0)
    elif order == 'top':
        if size == 0:
            print(-1)
        else:
            print(stack[-1])