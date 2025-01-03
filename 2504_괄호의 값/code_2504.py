# https://www.acmicpc.net/problem/2504
import sys
# sys.stdin = open('input_2504.txt')

temp = list(input().rstrip())
stack = []
ans = 0
now_int = 1

for i in range(len(temp)):
    if temp[i] == '(' or temp[i] == '[':
        stack.append(temp[i])
        if temp[i] == '(':
            now_int *= 2
        elif temp[i] == '[':
            now_int *= 3
    else:
        if not stack:
            ans = 0
            break
        last = stack.pop()
        now = temp[i]
        before = temp[i-1]
        if now == ')':
            if before == '[' or last =='[':
                ans = 0
                break
            elif before == '(':
                ans += now_int
            now_int //= 2
        elif now == ']':
            if before == '(' or last == '(':
                ans = 0
                break
            elif before == '[':
                ans += now_int
            now_int //= 3

if stack:
    print(0)
else:
    print(ans)
