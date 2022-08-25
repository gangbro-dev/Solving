import sys
sys.stdin = open('sample_input.txt')


def maze_run(start, maze, cnt):
    delta = [(1,0), (0,1), (-1,0), (0, -1)]

    for drow, dcolumn in delta:
            if 0 <= start[0] + drow < N and 0 <= start[1] + dcolumn < N:
                if maze[start[0] + drow][start[1] + dcolumn] == 3:
                    return cnt
                elif maze[start[0] + drow][start[1] + dcolumn]:
                    continue
                else:
                    maze[start[0] + drow][start[1] + dcolumn] = 1
                    ans = maze_run((start[0] + drow, start[1] + dcolumn), maze, cnt + 1)
                    if ans:
                        return ans
    return 0


T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    maze = [[int(x) for x in input()] for _ in range(N)]
    for row in range(len(maze)):
        if 2 in maze[row]:
            start = (row, maze[row].index(2))
            break

    print(f'#{Tc} {maze_run(start, maze, 0)}')
