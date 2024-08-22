# https://www.acmicpc.net/problem/14890
import sys
sys.stdin = open('input_14890.txt','r')
# T = int(input())
T = 4

def check_load(line):
    cnt = 1
    for i in range(N - 1):
        # 지금 타일과 다음 타일의 높이가 같은경우
        if line[i] == line[i + 1]:
            cnt += 1
        # 지금 타일보다 다음 타일이 1 높은 경우 and 낮은 타일이 x이상일 경우
        elif line[i + 1] - line[i] == 1 and cnt >= X:
            cnt = 1
        # 지금 타일보다 다음 타일이 1 낮은 경우 and 경사로 다음 바로 경사로 인지 확인
        elif line[i] - line[i + 1] == 1 and cnt >= 0:
            # 경사로의 X의 길이 이상인것을 체크용
            cnt = -X + 1
        # 높이가 2이상 차이날 경우
        else:
            return 0
    if cnt >= 0:
        return 1
    else:
        return 0


for test_case in range(1, T + 1):
    N, X = map(int, input().split())
    ans = 0

    ground = [list(map(int, input().split())) for _ in range(N)]
    rotate_ground = [[-1] * N for _ in range(N)]
    for i in range(N):
        ans += check_load(ground[i])
        for j in range(N):
            rotate_ground[i][j] = ground[N - j - 1][i]
    for i in range(N):
        ans += check_load(rotate_ground[i])

    print(f'#{test_case} {ans}')