# https://www.acmicpc.net/problem/14425
import sys
sys.stdin = open('input_14425.txt','r')

N,M = map(int,input().split())
string_set = set()
ans = 0
for _ in range(N):
    temp = input()
    string_set.add(temp)
for _ in range(M):
    temp = input()
    if temp in string_set:
        ans += 1
print(ans)