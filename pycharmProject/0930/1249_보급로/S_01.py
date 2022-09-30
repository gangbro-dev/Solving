import heapq

import sys
sys.stdin = open('input.txt')


def dijkstra(N, mat):
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    d_mat = [[-1] * N for _ in range(N)]
    now = (0, (0, 0))
    heap = [now]
    heapq.heapify(heap)
    while heap:
        now = heapq.heappop(heap)
        if now[1] == (N-1, N-1):
            break
        c_now = now[0]
        x, y = now[1]
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                cost = c_now + mat[nx][ny]
                if d_mat[nx][ny] < 0 or cost < d_mat[nx][ny]:
                    d_mat[nx][ny] = cost
                    heapq.heappush(heap, (cost, (nx, ny)))

    return d_mat[-1][-1]


T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    mat = [tuple(map(int, tuple(input()))) for _ in range(N)]

    print(f'#{Tc} {dijkstra(N, mat)}')
