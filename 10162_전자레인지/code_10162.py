# https://www.acmicpc.net/problem/10162
import sys
sys.stdin = open('input_10162.txt','r')

N = int(input())
if N%10 !=0 :
    print(-1)
else:
    ans = []
    ans.append(N//300)
    N = N % 300
    ans.append(N//60)
    N = N % 60
    ans.append(N//10)

    print(*ans)
