# https://www.acmicpc.net/problem/1019
import sys
sys.stdin = open('input_1019.txt')

def set_one(num):
    while num % 10 != 9:
        for i in str(num):
            ans[int(i)] += k
        num -= 1
    return num



N = int(input())
ans = [0] * 10
k = 1

while N > 0:
    N = set_one(N)

    if N < 10:
        for i in range(N+1):
            ans[i] += k
    else:
        for i in range(10):
            ans[i] += (N//10 +1)*k

    ans[0] -= k
    k *= 10
    N //= 10

print(*ans)

