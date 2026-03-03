# https://www.acmicpc.net/problem/16570
import sys
sys.stdin = open('input_16570.txt')
input = sys.stdin.readline

def make_LPS(temp):
    lps = [0] * N
    j = 0

    max_len,cnt = 0,0

    for i in range(1,N):
        while j > 0 and temp[i]!=temp[j]:
            j = lps[j-1]
        
        if temp[i]==temp[j]:
            j+=1
            lps[i] = j
            if j > max_len:
                cnt = 1
                max_len = j
            elif j == max_len:
                cnt += 1

    return max_len,cnt

N = int(input())
nums = list(map(int,input().split()))
nums.reverse()
max_len,cnt = make_LPS(nums)

if max_len == 0:
    print(-1)
else:
    print(max_len,cnt)