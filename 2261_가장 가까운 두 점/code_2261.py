# https://www.acmicpc.net/problem/2261
import sys
# sys.stdin =open('input_2261.txt','r')

def divide(start,end):
    global dist
    if start == end:
        return float('inf')
    if end-1 == start:
        return (dots[start][0] - dots[end][0])**2 + (dots[start][1] - dots[end][1])**2
    mid = (start+end)//2
    min_dist = min(divide(start, mid),divide(mid,end))

    temp = []
    for i in range(start,end+1):
        if (dots[mid][0] - dots[i][0]) ** 2 < min_dist:
            temp.append(dots[i])
    temp.sort(key= lambda x:x[1])

    M = len(temp)
    for i in range(M-1):
        for j in range(i+1,M):
            if (temp[i][1] - temp[j][1])**2 < min_dist:
                min_dist = min(min_dist,((temp[i][0]-temp[j][0])**2) + ((temp[i][1]-temp[j][1])**2))
            else:
                break
    return min_dist



N = int(input())
dots = [list(map(int,input().split())) for _ in range(N)]
dots.sort()

# dist = float('inf')

print(divide(0,N-1))