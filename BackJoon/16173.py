from collections import deque

N = int(input())

matrix = list()
for _ in range(N):
    matrix.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(N)]
q = deque()

visited[0][0] = True
q.append((0, 0,))

ans = "Hing"
while q:
    x, y = q.popleft()
    delta = matrix[x][y]
    if delta:
        dx, dy = x + delta, y + delta
        if dx < N and not visited[dx][y]:
            q.append((dx, y,))
            visited[dx][y] = True
        if dy < N and not visited[x][dy]:
            q.append((x, dy,))
            visited[x][dy] = True
    if visited[-1][-1]:
        ans = "HaruHaru"
        break

print(ans)
