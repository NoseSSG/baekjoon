# https://www.acmicpc.net/problem/2096
import sys
sys.stdin = open('input_2096.txt','r')

N = int(input())
start = list(map(int,input().split()))
max_score = start[:]
min_score = start[:]

for _ in range(N-1):
    temp = list(map(int,input().split()))
    max_score = [temp[0] + max(max_score[0],max_score[1]), temp[1] + max(max_score), temp[2] + max(max_score[1],max_score[2])]
    min_score = [temp[0] + min(min_score[0],min_score[1]), temp[1] + min(min_score), temp[2] + min(min_score[1],min_score[2])]

print(max(max_score),min(min_score))