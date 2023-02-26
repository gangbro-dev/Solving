from collections import deque

N, M = map(int, input().split())
matrix = list()
for _ in range(N):
    matrix.append(list(map(int, input().split())))
delta = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
# 상어의 위치정보 저장
visited = [[N * M] * M for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(M):
        if matrix[i][j]:
            visited[i][j] = 0
            q.append((i, j,))
#BFS
ans = 0
while q:
    x, y = q.popleft()
    for dx, dy in delta:
        nx, ny = x + dx, y+dy
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] > visited[x][y] + 1:
            visited[nx][ny] = visited[x][y] + 1
            if ans < visited[nx][ny]:
                ans = visited[nx][ny]
            q.append((nx, ny,))

print(ans)
