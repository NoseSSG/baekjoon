# https://www.acmicpc.net/problem/7662
import sys
sys.stdin = open('input_7662.txt','r')

import heapq

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    max_heap = []
    min_heap = []
    is_delete = [False] * N
    idx = 0
    for _ in range(N):
        order, num = map(str,input().split())
        if order == 'I':
            heapq.heappush(min_heap,(int(num),idx))
            heapq.heappush(max_heap,(-(int(num)),idx))
            idx += 1
        else:
            if int(num) == 1:
                if not max_heap: continue
                max_num,i = heapq.heappop(max_heap)

                while is_delete[i]:
                    if not max_heap: break
                    max_num, i = heapq.heappop(max_heap)
                is_delete[i] = True
            else:
                if not min_heap: continue
                min_num,i = heapq.heappop(min_heap)
                while is_delete[i]:
                    if not min_heap: break
                    max_num, i = heapq.heappop(min_heap)
                is_delete[i] = True

    max_ans = []
    min_ans = []
    for n,i in max_heap:
        if not is_delete[i]:
            heapq.heappush(max_ans,n)
    for n, i in min_heap:
        if not is_delete[i]:
            heapq.heappush(min_ans,n)
    # print(max_ans,min_ans)
    if max_ans or min_ans:
        print(-heapq.heappop(max_ans),heapq.heappop(min_ans))
    else:
        print('EMPTY')