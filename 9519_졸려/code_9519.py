# https://www.acmicpc.net/problem/9519
import sys

from audioop import reverse

# sys.stdin = open('input_9519.txt','r')

def reverse_word():
    first = word[0::2]
    second = word[1::2]
    second = second[::-1]
    return first+second

N = int(input())
origin = input()
word = origin
word_list = []
cnt = 1
for i in range(N):
    word = reverse_word()
    word_list.append(word)
    if word == origin:
        break
    cnt += 1

print(word_list[(N-1)%cnt])