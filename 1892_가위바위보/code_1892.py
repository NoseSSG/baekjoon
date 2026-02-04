# https://www.acmicpc.net/problem/1892
import sys
sys.stdin = open("input_1892.txt")
input = sys.stdin.readline
from fractions import Fraction

N,K = map(int,input().split())
DP = [[Fraction(0,1) for _ in range(K+1)] for _ in range(K+1)]
DP[0][0] = Fraction(1,1)

p = Fraction(1,3)

for _ in range(N):
    nxt = [[Fraction(0,1) for _ in range(K+1)] for _ in range(K+1)]

    for a in range(K+1):
        for b in range(K+1):
            cur = DP[a][b]
            if cur == 0:
                continue

            if a == K or b == K:
                nxt[a][b] += cur
                continue

            nxt[a+1][b] += cur * p

            nxt[a][b+1] += cur * p

            nxt[a][b] += cur * p

    DP = nxt
ans = Fraction(0,1)
for b in range(K):
    ans += DP[K][b]

print(ans.numerator,ans.denominator)