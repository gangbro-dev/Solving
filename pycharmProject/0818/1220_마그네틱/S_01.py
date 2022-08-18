import sys
sys.stdin = open('input.txt')

for Tc in range(1, 11):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for column in range(N):
        stack = []
        for row in range(N):
            if mat[row][column]:
                if not stack:
                    if mat[row][column] == 1:
                        stack.append(mat[row][column])
                else:
                    if stack[-1] != mat[row][column]:
                        stack.append(mat[row][column])
        cnt += len(stack)//2

    print(f'#{Tc} {cnt}')