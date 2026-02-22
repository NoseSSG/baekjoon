# https://www.acmicpc.net/problem/4796
import sys
sys.stdin = open('input_4796.txt')
input = sys.stdin.readline
case = 0
while 1:
    L,P,V = map(int,input().split())
    case += 1
    if L==P==V==0:
        break
    ans = 0
    time = V // P
    ans += time*L + min(L,V%P)
    print(f'Case {case}: {ans}')