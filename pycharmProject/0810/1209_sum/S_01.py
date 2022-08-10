import sys
sys.stdin = open('input.txt')

for x in range(1, 11):
    T = int(input())
    num_matrix = []
    for i in range(100):
        num_matrix.append(list(map(int, input().split())))
    sum_max = 0
    sum_now1 = 0
    sum_now2 = 0
    for i in range(100):
        # 가로합
        sum_now = 0
        for j in range(100):
            sum_now += num_matrix[i][j]
        if sum_now > sum_max:
            sum_max = sum_now
        # 세로합
        sum_now = 0
        for j in range(100):
            sum_now += num_matrix[j][i]
        if sum_now > sum_max:
            sum_max = sum_now
        # 대각합
        sum_now1 += num_matrix[i][i]
        sum_now2 += num_matrix[i][100-i-1]
    if sum_now1 > sum_max:
        sum_max = sum_now1
    if sum_now2 > sum_max:
        sum_max = sum_now2

    print(f'#{T} {sum_max}')
