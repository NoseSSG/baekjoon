# https://www.acmicpc.net/problem/11501
import sys
sys.stdin = open('input_11501.txt')

test_case = int(input())

for _ in range(test_case):
    day = int(input())
    price = list(map(int,input().split()))
    ans = 0
    max_price = 0
    for n_d in range(day-1,-1,-1):
        if price[n_d] > max_price:
            max_price = price[n_d]
        else:
            ans += max_price-price[n_d]
    print(ans)