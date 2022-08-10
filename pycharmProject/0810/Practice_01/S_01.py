import sys
sys.stdin = open('input.txt')

T = int(input())
# 좌 우 상 하 순으로 검색할 것
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
for Tc in range(1, T+1):
    num_list = []
    for i in range(5):
        num_list.append(list(map(int, input().split())))

    sum_abs = 0
    # 기준점 가로줄
    for i in range(5):
        # 기준점 세로줄
        for j in range(5):
            # 상하좌우
            for k in range(4):
                # 연산이 가능한가?
                if 0 <= i+dy[k] < 5 and 0 <= j+dx[k] < 5:
                    sum_abs += abs(num_list[i][j] - num_list[i+dy[k]][j+dx[k]])

    print(f'#{Tc} {sum_abs}')


