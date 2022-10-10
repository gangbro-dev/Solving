import sys
from collections import deque
input = sys.stdin.readline
delta = [(-1, 0), (0, -1), (0, 1), (1, 0)]

N = int(input())

mat = list()
for i in range(N):
    temp = list(map(int, input().split()))
    mat.append(temp)
    if 9 in temp:
        start = (i, temp.index(9))
size = 2
left = size
visited = [[0] * N for _ in range(N)]
q = deque()
q.append(start)

while True:
    while q:
        movable = list()
        eatable = list()
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if not visited[nx][ny] and mat[nx][ny] < size:
                eatable.append((nx, ny))



