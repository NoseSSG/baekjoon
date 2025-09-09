# https://www.acmicpc.net/problem/1707
import sys
sys.stdin = open('input_1707.txt','r')
from collections import deque

def bfs(start,group):
    queue = deque([start])
    visited[start] = group
    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = -1 * visited[x]
            elif visited[i] == visited[x]:
                return False
    return True


TESTCASE = int(input())
for T in range(TESTCASE):
    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False] * (V+1)

    for _ in range(E):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1,V+1):
        if not visited[i]:
            result = bfs(i,1)
            if not result:
                break
    print('YES' if result else 'NO')