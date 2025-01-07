# https://www.acmicpc.net/problem/4378
import sys
sys.stdin = open('input_4378.txt')

keyboard = "`1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./"
while 1:
    try:
        temp = input()
        ans = ''
        for i in temp:
            if i == ' ' or i =='':
                ans += i
            else:
                ans+=keyboard[keyboard.find(i)-1]
        print(ans)
    except:
        exit()
