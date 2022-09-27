import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    mat = [ list(map(int, input().split())) for _ in range()]
    # 좌상- 우하 대각선을 정리해보자
    # 좌상- 우하 대각선은 x = y + i 로 표현할 수 있다. (i = -(n-1) ~ n-1)
    # 처음과 끝은 포함되는 순간 성립할 수 없음 따라서 x - y = i [n-2: n+1]
    # 좌하- 우상 대각선을 정리해보자.
    # 좌하- 우상 대각선은 x + y = i 로 표현할 수 있다. i (0 ~ 2n-1
    # 마찬가지로 처음과 끝은 포함될 수 없다. 따라서 x + y = i [1: 2n-2]
    for i1 in range(N-2, N+1):                          # 서로 다른 대각선 4개를 순서 없이 선택한다.(조합)
        for i2 in range(i1 + 1, N+1):                   # 좌상- 우하 대각선 번호 i 2개
            for j1 in range(1, 2*N-2):
                for j2 in range(j1 + 1, 2*N-2):         # 좌하- 우상 대각선 번호 j 2개


    print(f'#{Tc} {}')
