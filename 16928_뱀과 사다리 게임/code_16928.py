# https://www.acmicpc.net/problem/16928
import sys
import heapq
sys.stdin = open('input_16928.txt','r')

def BFS(start):
    h_que = []
    heapq.heappush(h_que,(0,start))
    while h_que:
        cnt,now = heapq.heappop(h_que)
        if visited[now] !=0 and visited[now] < cnt:continue
        visited[now] = cnt
        if now >= 100:
            return cnt
        for i in range(6,0,-1):
            next_ = now + i
            while next_ in ladder_snake:
                next_ = ladder_snake[next_]
            if visited[next_] == 0:
                heapq.heappush(h_que,(cnt+1,next_))

ladder_snake = {}
N,M = map(int,input().split())
for _ in range(N+M):
    a,b = map(int,input().split())
    ladder_snake[a] = b
visited = [0]*107
ans = BFS(1)
print(ans)