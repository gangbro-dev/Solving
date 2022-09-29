import sys
sys.stdin = open('sample_input.txt')

T = int(input())
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for Tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    D_mat = [[-1] * N for _ in range(N)]
    D_mat[0][0] = 0
    visited = [[False] * N for _ in range(N)]
    now = (0, 0)
    next_set = set()
    while now != (N-1, N-1):
        x, y = now
        visited[x][y] = True
        next_set.discard((x, y))
        min_c = 9999999999
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if 0 <= x+dx < N and 0 <= y+dy < N:
                dist = mat[nx][ny] - mat[x][y]
                if dist < 0:
                    dist = 0                        # 높이차에 따른 비용
                cost = D_mat[x][y] + dist + 1       # 간선의 비용
                if D_mat[nx][ny] < 0 or D_mat[nx][ny] > cost:   # 출발점 + 현재 간선 비용이 도착점에 적힌 비용보다 크다면
                    D_mat[nx][ny] = cost
                    next_set.add((nx, ny))
                    if min_c > cost:
                        min_c = cost


        min_n = 99999999999
        for i, j in next_set:
            if not visited[i][j] and 0 < D_mat[i][j] < min_n:
                now = (i, j)
                min_n = D_mat[i][j]

    print(f'#{Tc} {D_mat[N-1][N-1]}')
