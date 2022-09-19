import sys
from collections import deque
sys.stdin = open('sample_input.txt')
T = int(input())
# pipe = [ # 초기버전
#     [],
#     [(1, 0, {1, 2, 4, 7}), (-1, 0, {1, 2, 5, 6}), (0, 1, {1, 3, 6, 7}), (0, -1, {1, 3, 4, 5})],
#     [(1, 0, {1, 2, 4, 7}), (-1, 0, {1, 2, 5, 6})],
#     [(0, 1, {1, 3, 6, 7}), (0, -1, {1, 3, 4, 5})],
#     [(-1, 0, {1, 2, 5, 6}), (0, 1, {1, 3, 6, 7})],
#     [(1, 0, {1, 2, 4, 7}), (0, 1, {1, 3, 6, 7})],
#     [(1, 0, {1, 2, 4, 7}), (0, -1, {1, 3, 4, 5})],
#     [(-1, 0, {1, 2, 5, 6}), (0, -1, {1, 3, 4, 5})]
# ]
pipe = [
    [],
    [(1, 0), (-1, 0), (0, 1), (0, -1)],
    [(1, 0), (-1, 0)],
    [(0, 1), (0, -1)],
    [(-1, 0), (0, 1)],
    [(1, 0), (0, 1)],
    [(1, 0), (0, -1)],
    [(-1, 0), (0, -1)]
]
for Tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    underground = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    underground = [[0] * (M + 2)] + underground + [[0] * (M + 2)]
    visited = [([0] * (M + 2)) for _ in range(N + 2)]
    start = (R+1, C+1)
    q = deque()
    q.append(start)
    visited[R+1][C+1] = 1
    ans = 0

    while q:
        x, y = q.popleft()
        if visited[x][y] <= L:
            ans += 1
        else:
            continue
        if underground[x][y]:
            for dx, dy in pipe[underground[x][y]]:
                if not visited[x+dx][y+dy] and (-dx, -dy) in pipe[underground[x+dx][y+dy]]:
                    q.append((x+dx, y+dy))
                    visited[x+dx][y+dy] = visited[x][y] + 1

    print(f'#{Tc} {ans}')
