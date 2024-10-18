# https://www.acmicpc.net/problem/1009
import sys
sys.stdin = open('input_1009.txt')

T = int(input())

for test_case in range(T):
    a,b = map(int,input().split())
    ans = 1
    for i in range(b):
        ans = (ans*a)%10
    if ans == 0: ans = 10
    print(ans)