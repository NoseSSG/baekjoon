# https://www.acmicpc.net/problem/6064
import sys
sys.stdin = open('input_6064.txt','r')

import math

T = int(input())
for test_case in range(T):
    N,M,x,y = map(int,input().split())
    LCM = int((N*M)/math.gcd(N,M))
    ans = -1
    time = 0
    while N*time <= LCM:
        if ((N*time + x)-y) % M == 0:
            ans = N*time + x
            break
        time += 1
    print(ans)