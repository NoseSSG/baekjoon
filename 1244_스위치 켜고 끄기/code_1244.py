# https://www.acmicpc.net/problem/1244
import sys
sys.stdin = open('input_1244.txt')
input = sys.stdin.readline

def boy_switch(n):
    for i in range(n-1,N,n):
        switches[i] = (switches[i]+1)%2

def girl_switch(n):
    i = n-1
    switches[i] = (switches[i]+1)%2
    for j in range(1,N):
        if 0<= i-j and i+j <N:
            if switches[i-j] == switches[i+j]:
                switches[i-j] = (switches[i-j]+1)%2
                switches[i+j] = (switches[i+j]+1)%2
            else:
                break

    

N = int(input())
switches = list(map(int,input().split()))
M = int(input())
for _ in range(M):
    a,b = map(int,input().split())
    if a == 1:
        # 남학생인 경우 -> 배수 스위치 변경
        boy_switch(b)
    else:
        # 여학생인 경우 -> 좌우 대칭인 경우까지 변경
        girl_switch(b)
for i,n in enumerate(switches):
    print(n,end=' ')
    if (i+1) % 20 == 0:
        print()