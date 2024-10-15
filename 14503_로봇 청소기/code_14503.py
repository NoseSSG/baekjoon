# https://www.acmicpc.net/problem/14503
import sys
sys.stdin = open('input_14503.txt','r')

N,M = map(int,input().split())
robot = list(map(int,input().split()))
room = [list(map(int,input().split())) for _ in range(N)]
print(room)