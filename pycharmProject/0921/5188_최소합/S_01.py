import sys
sys.stdin = open('sample_input.txt')


def minroute(N, x, y):
    if x == N and y == N:
        return sum


T = int(input())

for Tc in range(1, T+1):
    N = int(input())

    mat = [tuple(map(int, input().split())) for _ in range(N)]

    print(f'#{Tc} {mat}')
