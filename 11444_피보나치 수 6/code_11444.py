# https://www.acmicpc.net/problem/11444
import sys
sys.stdin = open('input_11444.txt','r')

def fibo(num):
    if num in fibo_dict: return fibo_dict[num]
    if num % 2 == 1:
        fibo_dict[num] = (fibo(num//2)**2 + fibo((num//2) +1)**2)%1000000007
    else:
        fibo_dict[num] = (fibo(num+1) - fibo(num-1))%1000000007
    return fibo_dict[num]

N = int(input())

fibo_dict = {0:0,1:1,2:1,3:2,4:3,5:5}
print(fibo(N)%1000000007)
