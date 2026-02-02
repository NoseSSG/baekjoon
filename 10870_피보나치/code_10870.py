# https://www.acmicpc.net/problem/10870
import sys
sys.stdin = open("input_10870.txt")
input = sys.stdin.readline

Fibo ={0:0,1:1,2:1}
n = int(input())

def find_fibo(N):
    if N in Fibo: return Fibo[N]
    Fibo[N] = find_fibo(N-1) + find_fibo(N-2)
    return Fibo[N]

print(find_fibo(n))