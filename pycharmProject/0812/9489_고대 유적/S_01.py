import sys
sys.stdin = open('input.txt')

T = int(input())

for Tc in range(1, T+1):
    N, M = map(int, input().split())
    mat = []
    for i in range(M):
        mat.append(list(map(int, input().split())))
    for column in range(M):
        for row in range(N):
            if mat
    print(f'#{Tc} {max_cnt}')