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
ans = 0
next_fish_flag = True

while next_fish_flag:
    # 먹이 새로 찾기 시작할 때 마다 리셋할 것: 시작점, 거리 카운트, 방문했느냐, 찾은 먹이들
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    visited[start[0]][start[1]] = 1
    eatable = list()
    q = [start]
    while not eatable:      # 먹이 찾을때 까지
        # 1단마다 리셋할 것 : 다음 찾을 칸들
        movable = list()
        cnt += 1
        for x, y in q:            # 1단 돌리기
            for dx, dy in delta:
                nx, ny = x+dx, y+dy
                if N <= nx or nx < 0 or N <= ny or ny < 0:
                    continue
                if not visited[nx][ny] and 0 < mat[nx][ny] < size:
                    eatable.append((nx, ny))
                elif not visited[nx][ny] and mat[nx][ny] <= size:
                    movable.append((nx, ny))
                visited[nx][ny] = 1
        if movable:
            q = movable
        else:
            next_fish_flag = False
            break
    if eatable:
        next_fish_flag = True
        # eatable.sort(key=lambda i: i[1])
        eatable.sort()
        # 상어 위치 이동
        mat[start[0]][start[1]] = 0
        start = eatable[0]
        mat[start[0]][start[1]] = 9
        # 거리 체크
        ans += cnt
        # 상어 성장 체크
        left -= 1
        if left == 0:
            size += 1
            left = size

print(ans)
