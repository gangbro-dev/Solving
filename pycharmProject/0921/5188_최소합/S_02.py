import sys                          # 실패
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    mat = [tuple(map(int, input().split())) for _ in range(N)]
    delta = [(1, 0), (0, 1)]
    path = 1 << ((N-1) * 2)

    minRoute = 10 * N * N
    for i in range(path):
        brute = format(i, '0' + str(((N-1) * 2)) + 'b')
        if sum(map(int, brute)) == N - 1:
            x = 0
            y = 0
            routeSum = mat[0][0]
            for d in brute:
                dx, dy = delta[int(d)]
                x += dx
                y += dy
                routeSum += mat[x][y]
                if routeSum > minRoute:
                    break
            else:
                minRoute = routeSum

    print(f'#{Tc} {minRoute}')
