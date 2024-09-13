# https://www.acmicpc.net/problem/1991
import sys
sys.stdin = open('input_1991.txt')

from collections import deque


def pre_ord(start):
    ans = ''
    temp = deque()
    temp.append(start)
    while temp:
        now = temp.popleft()
        ans += now
        if now in graph:

    pass


def in_ord(start):
    pass

def posr_ord(start):
    pass



graph = {}
N = int(input())
for _ in range(N):
    a,b,c = map(str,input().split())
    if a not in graph:
        graph[a] = []
    if b != '.':
        graph[a].append(b)
    if c != '.':
        graph[a].append(c)

