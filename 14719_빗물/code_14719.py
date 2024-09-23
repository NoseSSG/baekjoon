# https://www.acmicpc.net/problem/14719
import sys
sys.stdin = open('input_14719.txt','r')

H,W = map(int,input().split())
block = list(map(int,input().split()))
ans = 0
front = rear = 0
block_sum = 0

for idx in range(W):
    if block[front]==0:
        front = idx
        rear = idx
        continue
    rear = idx
    if front == rear:
        continue
    if block[rear] >= block[front]:
        print(((rear-front-1)*block[rear]))
        ans += ((rear-front-1)*block[rear]) - block_sum
        block_sum = 0
        front = idx
    else:
        block_sum += block[idx]
print(ans)




