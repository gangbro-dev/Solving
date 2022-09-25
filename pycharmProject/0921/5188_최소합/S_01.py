import sys
sys.stdin = open('sample_input.txt')

def minroute(N, mat, x, y, route):
    global min_result
    if x == N - 1 and y == N - 1:
        min_result = min(min_result, sum(route))
        return
    if sum(route) > min_result:
        return
    for dx, dy in [(1, 0), (0, 1)]:
        route_now = route[:]
        if x + dx < N and y + dy < N:
            route_now.append(mat[x+dx][y+dy])
            minroute(N, mat, x+dx, y+dy, route_now)



T = int(input())

for Tc in range(1, T+1):
    global min_result
    N = int(input())
    min_result = 10*N*N
    mat = [tuple(map(int, input().split())) for _ in range(N)]
    minroute(N, mat, 0, 0, [mat[0][0]])

    print(f'#{Tc} {min_result}')
