# https://www.acmicpc.net/problem/12756
import sys
sys.stdin = open('input_12756.txt')
input = sys.stdin.readline

def use_turn(attack,health):
    turn = health//attack
    if health % attack:
        turn += 1
    return turn

A = list(map(int,input().split()))
B = list(map(int,input().split()))

a_turn = use_turn(A[0],B[1])
b_turn = use_turn(B[0],A[1])

if a_turn < b_turn:
    print("PLAYER A")
elif a_turn > b_turn:
    print("PLAYER B")
else:
    print("DRAW")