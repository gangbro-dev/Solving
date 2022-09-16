from pprint import pprint
def solution(board, skill):
    cum_sum = [[0] * (len(board) + 1) for _ in range(len(board[0]) + 1)]
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            degree = -degree
        cum_sum[r1][c1] += degree
        cum_sum[r1][c2+1] -= degree
        cum_sum[r2+1][c1] -= degree
        cum_sum[r2+1][c2+1] += degree
    pprint(cum_sum)
    # 누적합 계산
    for row in range(len(board)):
        for column in range(len(board[0])):
            cum_sum[row][column+1] += cum_sum[row][column]
    for column in range(len(board[0])):
        for row in range(len(board)):
            cum_sum[row+1][column] += cum_sum[row][column]
    pprint(cum_sum)
    answer = 0
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] + cum_sum[row][column] > 0:
                answer += 1
    return answer

board = [
    [5,5,5,5,5],
    [5,5,5,5,5],
    [5,5,5,5,5],
    [5,5,5,5,5],
    [5,5,5,5,5],
]
skill = [
    [1, 0, 0, 3, 4, 4],
    [1, 2, 0, 2, 3, 2],
    [2, 1, 0, 3, 1, 2],
    [1, 0, 1, 3, 3, 1]
]
print(solution(board, skill))