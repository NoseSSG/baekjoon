# https://www.acmicpc.net/problem/14908
import sys
sys.stdin = open('input_14908.txt','r')

N = int(input())
shoes = [list(map(int,input().split()))+[i] for i in range(1,N+1)]
shoes.sort(key = lambda x : (x[1]/x[0]) ,reverse=True)
print(*list(map(lambda x :x[2],shoes)))