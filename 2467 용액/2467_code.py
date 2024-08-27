# https://www.acmicpc.net/problem/2467
import sys
sys.stdin = open('input_2467.txt','r')

T = 2
for test_case in range(1,T+1):
    N = int(input())
    temp = list(map(int,input().split()))
    start = 0
    end = N-1
    min_sum = float('inf')
    while True:
        if end <= start:
            break
        sample_sum = temp[start] + temp[end]
        if abs(sample_sum) < min_sum:
            min_sum = abs(sample_sum)
            ans = [temp[start],temp[end]]
        if sample_sum < 0: start +=1
        else: end -= 1

    print(*ans)