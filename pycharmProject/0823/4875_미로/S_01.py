import sys
sys.stdin = open('sample_input.txt')


def maze_run(start, maze):
    delta = [(1,0), (0,1), (-1,0), (0, -1)]

    for drow, dcolumn in delta:
            if 0 <= start[0] + drow < N and 0 <= start[1] + dcolumn < N:
                if maze[start[0] + drow][start[1] + dcolumn] == 3:
                    return 1
                elif maze[start[0] + drow][start[1] + dcolumn]:
                    continue
                else:
                    maze[start[0] + drow][start[1] + dcolumn] = 1
                    if maze_run((start[0] + drow, start[1] + dcolumn), maze):
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