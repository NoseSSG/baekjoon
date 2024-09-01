# https://www.acmicpc.net/problem/1711
import sys
sys.stdin = open('input_1711.txt','r')
T = int(input())
temp = [tuple(map(int,input().split()))for _ in range(T)]
ans = 0
for i in range(T-2):
    for j in range(i+1,T-1):
        for k in range(j+1,T):
            a,b,c = temp[i],temp[j],temp[k]
            x = (a[0]-b[0])**2 + (a[1]-b[1])**2
            y = (a[0]-c[0])**2 + (a[1]-c[1])**2
            z = (b[0]-c[0])**2 + (b[1]-c[1])**2
            if (x + y) == z or (x+z) == y or (y+z) == x : ans += 1
print(ans)


# combination을 사용할시 시간 초과 발생
# from itertools import combinations
# comb = combinations(temp,3)
# for i in comb:
#     a,b,c = i[0],i[1],i[2]
#     x = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
#     y = (a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2
#     z = (b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2
#     if (x + y) == z or (x + z) == y or (y + z) == x: ans += 1
# print(ans)