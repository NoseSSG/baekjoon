# https://www.acmicpc.net/problem/1305
import sys
sys.stdin = open('input_1305.txt')
input = sys.stdin.readline

def make_LPS(temp):
    LPS = [0] * (L)
    j = 0

    for i in range(1,L):
        while j > 0 and temp[i] != temp[j]:
            j = LPS[j-1]
        if temp[i] == temp[j]:
            j+=1
            LPS[i] = j
    return LPS


L = int(input())
ad = input().rstrip()
lps = make_LPS(ad)
print(L-lps[-1])