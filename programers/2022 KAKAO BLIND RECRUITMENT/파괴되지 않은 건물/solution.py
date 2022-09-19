def solution(board, skill):
    answer = len(board) * len(board[0])
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            degree = -degree

        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                temp = board[r][c]
                board[r][c] += degree
                if temp <= 0 < board[r][c]:
                    answer += 1
                elif board[r][c] <= 0 < temp:
                    answer -= 1

    return answer

# 정확성 100, 효율성 0