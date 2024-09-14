# https://www.acmicpc.net/problem/25498
import sys
# sys.stdin = open('input_25498.txt','r')
from collections import deque

def BFS(start):
    global ans
    d_que = deque()
    d_que.append((start,0))
    temp_que = deque()
    while d_que or temp_que:
        if d_que:
            now,idx = d_que.popleft()
            if len(ans) == idx: ans += char[now]
            visited.add(now)
            for next_ in graph[now]:
                if next_ in visited: continue
                if not temp_que:
                    temp_que.append((next_,idx+1))
                else:
                    if char[temp_que[-1][0]] < char[next_]:
                        temp_que.clear()
                        temp_que.append((next_,idx+1))
                    elif char[temp_que[-1][0]] == char[next_]:
                        temp_que.append((next_,idx+1))
        else:
            now, idx = temp_que.popleft()
            if len(ans) == idx: ans += char[now]
            visited.add(now)
            for next_ in graph[now]:
                if next_ in visited: continue
                if not d_que:
                    d_que.append((next_, idx + 1))
                else:
                    if char[d_que[-1][0]] < char[next_]:
                        d_que.clear()
                        d_que.append((next_, idx + 1))
                    elif char[d_que[-1][0]] == char[next_]:
                        d_que.append((next_, idx + 1))



N = int(input())
graph = {}
char = list(map(str,input().rstrip()))
visited = set()
for _ in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    if a not in graph:
        graph[a] = []
        graph[a].append(b)
    else:
        if char[graph[a][-1]] <= char[b]:
            if char[graph[a][-1]] == char[b]:
                graph[a] = [b]
            else:
                graph[a].append(b)
    if b not in graph:
        graph[b] = []
        graph[b].append(a)
    else:
        if char[graph[b][-1]] <= char[a]:
            if char[graph[b][-1]] == char[a]:
                graph[b] = [a]
            else:
                graph[b].append(a)
ans = ''
BFS(0)
print(ans)