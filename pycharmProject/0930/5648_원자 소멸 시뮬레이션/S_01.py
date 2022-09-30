from collections import deque

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
direction = {0: (0, 1), 1: (0, -1), 2: (-1, 0), 3:(1, 0)}
for Tc in range(1, T+1):
    N = int(input())
    field = [[0] * 2001 for _ in range(2001)]
    q = deque()
    for __ in range(N):
        x, y, direc, E = map(int, input().split())
        q.append((direc, (x, y)))
        field[x][y] = (E, 0)

    ans = 0

    while len(q) > 1:
        move = q.popleft()
        direc = move[0]
        x, y = move[1]
        if not field[x][y]: # 충돌로 소멸했다면, 넘기기
            continue
        E = field[x][y]
        dx, dy = direction[direc]
        nx, ny = x+dx, y+dy
        if 1000 < nx < -1000 or 1000 < ny < -1000:  # 외부로 방출
            field[x][y] = 0
            continue
        else:
            if field[nx][ny]:
                if field[x][y][1] == ??? # 충돌 : 에너지 방출 후 소멸 (원래 있던 놈은 어카지?)
                ans += field[nx][ny] + field[x][y]
                field[nx][ny] = field[x][y] = 0

            else:                   # 충돌하지 않음
                field[nx][ny], field[x][y] = field[x][y], 0
                q.append((direc, (nx, ny)))

    print(f'#{Tc} {ans}')
