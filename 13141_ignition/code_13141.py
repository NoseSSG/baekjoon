# https://www.acmicpc.net/problem/13141
import sys
sys.stdin = open('input_13141.txt')

def floyd_warshall():
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i == j: continue
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

def ignition(start):
    result = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if not max_dist[i][j]: continue
            # short,long = sorted([dist[start][i], dist[start][j]])
            short,long = (dist[start][i],dist[start][j]) if dist[start][i] <= dist[start][j] else (dist[start][j],dist[start][i])
            remain = max_dist[i][j] - (long-short)
            result = max(result, long + remain/2)
    return result

n,m = map(int,input().split())
dist = [[0 if i==j else float('inf') for j in range(n+1) ] for i in range(n+1)]
max_dist = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    s,e,l = map(int,input().split())
    # floyd_warshall 최소거리 저장
    dist[s][e] = min(dist[s][e],l)
    dist[e][s] = min(dist[e][s],l)
    # innition 최대거리 저장
    max_dist[s][e] = max(max_dist[s][e],l)
    max_dist[e][s] = max(max_dist[e][s],l)  

floyd_warshall()

ans = float('inf')
for node in range(1,n+1):
    time = ignition(node)
    ans = min(ans,time)
print(ans)