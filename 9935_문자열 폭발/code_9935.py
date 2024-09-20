# https://www.acmicpc.net/problem/9935
import sys
# sys.stdin = open('input_9935.txt','r')

first_text = input()
second_text = input()
len_fir = len(first_text)
len_sec = len(second_text)
ans = []
for i in range(len(first_text)):
    ans.append(first_text[i])
    if len(ans) >= len_sec and ''.join(ans[-len_sec:]) == second_text:
        for _ in range(len_sec):
            ans.pop()
if ans:
    print(''.join(ans))
else:
    print('FRULA')