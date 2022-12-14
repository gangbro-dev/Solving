import heapq
DELTA = ((-1, 0), (0, -1), (1, 0), (0, 1),)
N, M, K = map(int, input().split())

ores = list()
for _ in range(N):
    ores.append(tuple(map(int, input().split())))

visited = [[False] * M for _ in range(N)]
q = list()

# 첫 테두리 힙에 넣기
if M == 1:
    for i in range(N):
        heapq.heappush(q, (ores[i][0], i, 0))
        visited[i][0] = True
else:
    for j in range(M):
        heapq.heappush(q, (ores[0][j], 0, j))
        visited[0][j] = True
    for i in range(1, N):
        for j in (0, M-1):
            heapq.heappush(q, (ores[i][j], i, j))
            visited[i][j] = True
# 시작할 수 있는 돌 강도
S = 0
cnt = 0
# 돌 하나씩 쪼개보자 -> 내가 원하는 만큼 쪼갯으면 끗
while q and cnt < K:
    ore = heapq.heappop(q)
    if ore[0] > S:
        S = ore[0]
    cnt += 1
    x, y = ore[1], ore[2]
    for dx, dy in DELTA:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            heapq.heappush(q, (ores[nx][ny], nx, ny))
            visited[nx][ny] = True

print(S)
