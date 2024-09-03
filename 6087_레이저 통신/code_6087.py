# https://www.acmicpc.net/problem/6087
import sys
sys.stdin = open('input_6087.txt','r')

W,H = map(int,input().split())
temp = [list(map(str,input().split())) for _ in range(H)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
