# https://www.acmicpc.net/problem/1491
N,M = map(int,input().split())

length = N*M -1
aaa = [N-1] + list(range(N-1,-1,-1))
bbb = list(range(M-1,-1,-1))

i = 0
j = 0
flag = 0
x = 0
y = 0
while length>0:
    if flag%2 == 0:
        if flag == 0:
            x += aaa[i]
        else:
            x -= aaa[i]
        length -= aaa[i]
        i += 1
    else:
        if flag == 1:
            y += bbb[j]
        else:
            y -= bbb[j]
        length -= bbb[j]
        j +=1
    flag = (flag+1)%4

print(x,y)