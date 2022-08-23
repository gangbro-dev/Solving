import sys
sys.stdin = open('sample_input.txt')


def maze_run(start, maze):
    drow = [1, 0, -1, 0]
    dcolumn = [0, 1, 0, -1]

    for row in range(4):
        for column in range(4):
            if 0 <= start[0] + drow[row] < N and 0 <= start[1] + dcolumn[column] < N:
                if maze[start[0] + drow[row]][start[1] + dcolumn[column]] == 3:
                    return 1
                elif maze[start[0] + drow[row]][start[1] + dcolumn[column]]:
                    continue
                else:
                    maze[start[0] + drow[row]][start[1] + dcolumn[column]] = 1
                    if maze_run((start[0] + drow[row], start[1] + dcolumn[column]), maze):
                        return 1
    return 0


T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    maze = [[int(x) for x in input()] for _ in range(N)]
    start = ()
    for row in range(N):
        for column in range(N):
            if start:
                break
            if maze[row][column] == 2:
                start = (row, column)
        if start:
            break

    print(f'#{Tc} {maze_run(start, maze)}')