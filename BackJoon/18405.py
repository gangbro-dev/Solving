from sys import stdin
from collections import deque
from pprint import pprint

input = stdin.readline
delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]
N, K = map(int, input().split())
matrix = list()
virus = dict()
for i in range(N):
    matrix.append(list(map(int, input().split())))
    # 각 바이러스의 위치 저장
    for j in range(N):
        if matrix[i][j]:
            if matrix[i][j] in virus.keys():
                virus[matrix[i][j]].append((i, j,))
            else:
                virus[matrix[i][j]] = [(i, j,)]
# 밑준비
count, a, b = map(int, input().split())
a, b = a - 1, b - 1     # 인덱스와 맞춰준다.
nq = list()
# 번호 순 대로 큐에 입력
q = deque()

for k in sorted(virus.keys()):
    for V in virus[k]:
        q.append(V)
#BFS 시작
while q:
    if not count:
        break
    x, y = q.popleft()
    for dx, dy in delta:
        nx, ny = x + dx, y+dy
        if 0 <= nx < N and 0 <= ny < N and not matrix[nx][ny]:
            matrix[nx][ny] = matrix[x][y]
            nq.append((nx, ny,))
            # 만약, 목표로 하는 칸이 채워졌다면, 반복을 종료하고 빠져나온다.
            if nx == a and ny == b:
                q = deque()
                break
    if not q:
        q = deque(nq)
        nq = list()
        count -= 1

print(matrix[a][b])
