from collections import deque
M, N, H = map(int, input().split())

box = []
boxes = []
for k in range(H):
    box = []
    for j in range(N):
        box.append(list(map(int, input().split())))
    boxes.append(box[:])

delta = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

q = deque()

visited = [[[0] * M for _ in range(N)] for __ in range(H)]
for k in range(H):
    for j in range(N):
        for i in range(M):
            if boxes[k][j][i] == 1:
                q.append((k, j, i))
                visited[k][j][i] = 1

while q:
    k, j, i = q.popleft()
    for dk, dj, di in delta:
        if 0 <= k + dk < H and 0 <= j + dj < N and 0 <= i + di < M:
            if not boxes[k+dk][j+dj][i+di]:
                boxes[k+dk][j+dj][i+di] = 1
                q.append((k+dk, j+dj, i+di))
                visited[k+dk][j+dj][i+di] = visited[k][j][i] + 1

nomat_flag = False
max_day = 0
for k in range(H):
    for j in range(N):
        for i in range(M):
            if not boxes[k][j][i]:
                nomat_flag = True
                break
            else:
                max_day = max(visited[k][j][i], max_day)
        if nomat_flag:
            break
    if nomat_flag:
        break

if nomat_flag:
    print(-1)
else:
    print(max_day-1)