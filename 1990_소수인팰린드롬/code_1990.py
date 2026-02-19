# https://www.acmicpc.net/problem/1990
import sys
sys.stdin = open('input_1990.txt')
input = sys.stdin.readline
import math

def is_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    r = int(math.isqrt(x))
    d = 3
    while d <= r:
        if x % d == 0:
            return False
        d += 2
    return True

def make_pal(half):
    s = str(half)
    return int(s + s[-2::-1])

a, b = map(int, input().split())
if a > b:
    a, b = b, a

for i in range(max(2, a), min(10, b + 1)):
    if is_prime(i):
        print(i)

if a <= 11 <= b:
    print(11)

for half in range(10, 100000):
    pal = make_pal(half)
    
    if pal > b:
        break
    if pal < a:
        continue
    
    if is_prime(pal):
        print(pal)

print(-1)
