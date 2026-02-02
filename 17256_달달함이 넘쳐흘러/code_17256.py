# https://www.acmicpc.net/problem/17256
import sys
sys.stdin = open('input_17256.txt')
input = sys.stdin.readline

ax,ay,az = map(int,input().split())
cx,cy,cz = map(int,input().split())

print(cx-az,cy//ay,cz-ax)