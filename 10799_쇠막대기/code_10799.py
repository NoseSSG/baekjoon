# https://www.acmicpc.net/problem/10799
import sys
# sys.stdin = open('input_10799.txt','r')

laser_stick = input()
before = ''
stack = []
ans = 0
for now in laser_stick:
    if before == '(' and now == ')':
        stack.pop()
        ans += len(stack)
    elif now == ')':
        stack.pop()
        ans += 1
    else:
        stack.append(now)

    before = now
print(ans)
