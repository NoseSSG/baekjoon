# https://www.acmicpc.net/problem/1786
import sys
sys.stdin = open('input_1786.txt')
input = sys.stdin.readline

def make_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    
    length = 0  # 현재까지 일치한 prefix 길이
    i = 1       # lps[0]은 항상 0이므로 1부터 시작
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
                
    return lps


T = input().rstrip('\n')
P = input().rstrip('\n')

LPS = make_lps(P)

i = 0 
j = 0
ans = 0
pos =[]


while i < len(T):
    if T[i] == P[j]:
        i += 1
        j += 1
    
    if j == len(P):
        ans += 1
        pos.append(i-j+1)
        j = LPS[j-1]
    
    elif i < len(T) and T[i] != P[j]:
        if j != 0:
            j = LPS[j-1]
        else:
            i += 1
print(ans)
for p in pos:
    print(p,end=' ')