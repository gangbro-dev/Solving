import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    N = int(input())

    mexinos = [list(map(int, input().split())) for _ in range(N)]
    core = []
    connect = []
    left = []
    line_cnt = 0
    for row in range(N):
        for column in range(N):
            if mexinos[row][column] == 1:
                core.append((row, column))
                if not row or not column:
                    connect.append((row, column))
                elif row == N - 1 or column == N - 1:
                    connect.append((row, column))
    # 최소길이 결선이 가능한 외곽칩부터 결선
    for i in range(1, N // 2):
        for chip in core:
            if chip in connect:
                continue

            if chip[0] <= 0 + i:
                for j in range(0 + i):
                    if mexinos[j][chip[1]]:
                        break
                else:
                    for j in range(0 + i):
                        mexinos[j][chip[1]] = 2
                        line_cnt += 1
                    connect.append(chip)

            elif chip[0] >= (N - 1) - i:
                for j in range(N - i, N):
                    if mexinos[j][chip[1]]:
                        break
                else:
                    for j in range(N - i, N):
                        mexinos[j][chip[1]] = 2
                        line_cnt += 1
                    connect.append(chip)

            elif 0 + i >= chip[1]:
                for j in range(0 + i):
                    if mexinos[chip[0]][j]:
                        break
                else:
                    for j in range(0 + i):
                        mexinos[chip[0]][j] = 2
                        line_cnt += 1
                    connect.append(chip)

            elif chip[1] >= (N - 1) - i:
                for j in range((N) - i, N):
                    if mexinos[chip[0]][j]:
                        break
                else:
                    for j in range(N - i, N):
                        mexinos[chip[0]][j] = 2
                        line_cnt += 1
                    connect.append(chip)
    past_left = []
    while True:
        left = []
        for i in core:
            if i not in connect:
                left.append(i)
        if left == past_left:
            break
        # 남은 칩 최소 길이로 결선
        # 칩 중에 한 가지 방법밖에 없는 칩부터 연결하고 나머지를
        # 좌 상 우 하 순으로 체크하자
        delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        way_cnt = [[20, 20, 20, 20] for _ in range(len(left))]
        for left_i in range(len(left)):

            for x in range(left[left_i][0]):
                if mexinos[x][left[left_i][1]]:
                    break
            else:
                way_cnt[left_i][0] = left[left_i][0]
            for y in range(left[left_i][1]):
                if mexinos[left[left_i][0]][y]:
                    break
            else:
                way_cnt[left_i][1] = left[left_i][1]
            for x in range(left[left_i][0] + 1, N):
                if mexinos[x][left[left_i][1]]:
                    break
            else:
                way_cnt[left_i][2] = N - left[left_i][0] - 1
            for y in range(left[left_i][1] + 1, N):
                if mexinos[left[left_i][0]][y]:
                    break
            else:
                way_cnt[left_i][3] = N - left[left_i][1] -1
        # 남은 칩에서 연결 가능한지 체크. 모두 불가능하다면, 탈출
        for i in way_cnt:
            if i != [20, 20, 20, 20]:
                break
        else:
            break

        # 연결 가능한 방법이 1개인 칩들을 먼저 연결-> 연결선이 짧은 순서대로 연결
        # 연결 가능한 방법이 2개인 칩들을 연결 -> 연결선이 짧은 순서대로 연결
        # 연결 가능한 방법이 3개인 칩들을 연결 -> 연결선이 짧은 순서대로 연결
        temp = [0, 1]
        for method in range(3, 0, -1):
            break_flag = False
            for chip in left:
                if way_cnt[left.index(chip)].count(20) == method:
                    temp = (chip, min(way_cnt[left.index(chip)]))
                    break
            if temp[0]:
                break
        for i in range(4):
            if way_cnt[left.index(temp[0])][i] == temp[1]:
                connect.append(temp[0])
                x, y = temp[0]
                dx, dy = delta[i]
                x = x + dx
                y = y + dy
                while 0 <= x < N and 0 <= y < N:
                    mexinos[x][y] = 2
                    line_cnt += 1
                    x = x + dx
                    y = y + dy
                break

        past_left = left[:]

    print(f'#{Tc} {line_cnt}')


