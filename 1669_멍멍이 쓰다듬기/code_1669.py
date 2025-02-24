# https://www.acmicpc.net/problem/1669
import sys
sys.stdin = open('input_1669.txt')

def solve(num):
    ans = 0
    temp = 1
    while True:
        for i in range(2):
            if num <=0:
                return ans
            ans += 1
            num -= temp
        temp += 1

N,M = map(int,input().split())
diff = abs(N-M)
print(solve(diff))