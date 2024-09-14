# https://www.acmicpc.net/problem/1991
import sys
# sys.stdin = open('input_1991.txt')

def pre_ord(start):
    if start == '.':
        return
    print(start,end='')
    pre_ord(graph[start][0])
    pre_ord(graph[start][1])


def in_ord(start):
    if start == '.':
        return
    in_ord(graph[start][0])
    print(start,end='')
    in_ord(graph[start][1])

def post_ord(start):
    if start == '.':
        return
    post_ord(graph[start][0])
    post_ord(graph[start][1])
    print(start, end='')



graph = {}
N = int(input())
for _ in range(N):
    a,b,c = map(str,input().split())
    if a not in graph:
        graph[a] = []
    graph[a].append(b)
    graph[a].append(c)

pre_ord('A')
print()
in_ord('A')
print()
post_ord('A')
print()