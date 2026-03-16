# https://www.acmicpc.net/problem/1135
import sys
sys.stdin = open('input_1135.txt')
input = sys.stdin.readline

def count_time(head):
    if head not in tree:
        return 0

    times = []
    for c in tree[head]:
        times.append(count_time(c))

    times.sort(reverse=True)

    max_finish = 0
    for idx, t in enumerate(times):
        max_finish = max(max_finish, t + (idx + 1))

    return max_finish
    


N = int(input())
heads = list(map(int,input().split()))
child = [0] * (N)
tree = {}
for i in range(1,N):
    if heads[i] not in tree:
        tree[heads[i]] = []
    tree[heads[i]].append(i)
    child[heads[i]] += 1
print(count_time(0))