# https://www.acmicpc.net/problem/10158
import sys
sys.stdin = open('input_10158.txt')


w,h = map(int,input().split())
p,q = map(int,input().split())
t = int(input())

x = w - abs(w - (p+t)%(2*w))
y = h - abs(h - (q+t)%(2*h))

print(x,y)