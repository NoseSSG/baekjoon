# https://www.acmicpc.net/problem/25637
import sys
# sys.stdin = open('input_25637.txt','r')

def brute_force(cnt):
    global ans
    if not zero_idx:
        ans = min(ans,cnt)
    if cnt >= ans: return
    for many_people_idx in list(many_people):
        for zero_people_idx in list(zero_idx):
            people[many_people_idx] -= 1
            people[zero_people_idx] += 1
            zero_idx.discard(zero_people_idx)
            if people[many_people_idx] == 1:
                many_people.discard(many_people_idx)
                brute_force(cnt+min(abs(many_people_idx-zero_people_idx),abs(many_people_idx - (zero_people_idx-N))))
                many_people.add(many_people_idx)
            else:
                brute_force(cnt + min(abs(many_people_idx-zero_people_idx),abs(many_people_idx - (zero_people_idx-N))))
            people[many_people_idx] += 1
            people[zero_people_idx] -= 1
            zero_idx.add(zero_people_idx)


T = 2
# for test_case in range(1,T+1):
N = int(input())
people = list(map(int,input().split()))
ans = float('inf')
zero_idx = set()
many_people = set()
for i in range(N):
    if people[i] == 0:
        zero_idx.add(i)
    elif people[i] > 1:
        many_people.add(i)
brute_force(0)
print(ans)