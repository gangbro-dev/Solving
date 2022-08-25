from collections import deque
import sys
sys.stdin = open('input.txt')


def maze_run(maze, start):
    visited = [[-1] * maze_size for _ in range(maze_size)]
    visited[start[0]][start[1]] = 0
    q = deque()
    q.append(start)
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    ans = 0

    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            if maze[x + dx][y + dy] == 3:
                ans = 1
                q.clear()
                break
            if not maze[x + dx][y + dy] and visited[x + dx][y + dy] < 0:
                q.append((x + dx, y + dy))
                visited[x + dx][y + dy] = visited[x][y] + 1

    return ans


for Tc in range(1, 11):
    T = int(input())
    maze_size = 16
    maze = []
    for row in range(maze_size):
        maze.append(list(map(int, [*input()])))
        if 2 in maze[-1]:
            start = (row, maze[-1].index(2))
        if 3 in maze[-1]:
            end = (row, maze[-1].index(3))

    print(f'#{Tc} {maze_run(maze, start)}')
