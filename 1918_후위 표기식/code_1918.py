# https://www.acmicpc.net/problem/1918
import sys
sys.stdin = open('input_1918.txt','r')

line = input()
ans =''
temp = []
for i in line:
    if i == '(':
        temp.append(i)
    elif i == ')':
        while temp and temp[-1] != '(':
            ans += temp.pop()
        temp.pop()
    elif i == '*' or i == '/':
        while temp and (temp[-1] == '/' or temp[-1] == '*'):
            ans += temp.pop()
        temp.append(i)
    elif i == '+' or i == '-':
        while temp and temp[-1] != '(':
            ans += temp.pop()
        temp.append(i)
    else:
        ans += i
    # print(temp,ans)
while temp:
    ans += temp.pop()
print(ans)
