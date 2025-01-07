# https://www.acmicpc.net/problem/2179
import sys
sys.stdin = open('input_2179.txt')

def count_head(a,b):
    cnt = 0
    if a == b:
        return 0
    
    for i in range(min(len(a),len(b))):
        if a[i]!=b[i]:
            break
        cnt += 1
    return cnt


N = int(input())
temp = list(input() for _ in range(N))
sort_word = sorted(list(enumerate(temp)),key = lambda x:x[1])

max_head = 0
max_length = [0] * N

for i in range(N-1):
    a = sort_word[i]
    b = sort_word[i+1]
    
    tmp = count_head(a[1],b[1])
    max_head = max(max_head,tmp)
    # if max_head == tmp:
    max_length[a[0]] = max(max_length[a[0]],tmp)
    max_length[b[0]] = max(max_length[b[0]],tmp)

check_length = 0

for i in range(N):
    if check_length == 0:
        if max_head == max_length[i]:
            check_length = temp[i]
            print(temp[i])
            pre = temp[i][:max_head]
    else:
        if max_head == max_length[i] and temp[i][:max_head] == pre:
            print(temp[i])
            break