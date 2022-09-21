def solution(board, skill):
    N = len(board)
    M = len(board[0])
    cum_sum = [[0] * (M + 1) for _ in range(N + 1)]
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            degree = -degree
        cum_sum[r1][c1] += degree
        cum_sum[r1][c2+1] -= degree
        cum_sum[r2+1][c1] -= degree
        cum_sum[r2+1][c2+1] += degree

    # 누적합 계산
    for row in range(len(board)):
        for column in range(len(board[0])):
            cum_sum[row][column+1] += cum_sum[row][column]

    for column in range(len(board[0])):
        for row in range(len(board)):
            cum_sum[row+1][column] += cum_sum[row][column]

    answer = 0
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] + cum_sum[row][column] > 0:
                answer += 1
    return answer
