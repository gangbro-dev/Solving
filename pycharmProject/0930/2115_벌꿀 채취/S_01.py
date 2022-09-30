import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    N, M, C = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    value_mat = [[-1] * (N - M + 1) for _ in range(N)]

    for i in range(N):
        for j in range(N - M + 1):
            work_area = mat[i][j:j+M]
            work_area.sort()
            while work_area:
                skip_flag = False
                work_left = C
                work_value = 0
                k = 0
                while k < len(work_area):
                    if work_left < work_area[~k]:
                        skip_flag = True
                    else:
                        work_left -= work_area[~k]
                        work_value += work_area[~k] ** 2
                    k += 1
                value_mat[i][j] = max(work_value, value_mat[i][j])
                if not skip_flag:
                    break
                work_area.pop()
    max_work = 0
    max_idx = (-1, -1)
    second_max_work = 0
    for i in range(N):
        for j in range(N - M + 1):
            if max_work < value_mat[i][j]:
                max_work = value_mat[i][j]
                max_idx = (i, j)
    for i in range(max_idx[1] - M + 1, max_idx[1] + M):
        if  0 <= i < N - M + 1:
            value_mat[max_idx[0]][i] = -1
    for i in range(N):
        for j in range(N - M + 1):
            if second_max_work < value_mat[i][j]:
                second_max_work = value_mat[i][j]
    ans = max_work + second_max_work

    print(f'#{Tc} {ans}')
