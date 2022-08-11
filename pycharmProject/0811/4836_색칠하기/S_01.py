import sys
sys.stdin = open('input.txt')

T = int(input())

for Tc in range(1, T+1):
    mat = [[0]*10 for _ in range(10)]
    N = int(input())
    r1 = []     # 왼쪽 위 모서리 좌표 넣어두기
    r2 = []     # 오른쪽 아래 모서리 좌표 넣어두기
    clr = []    # 색칠 값 넣어두기
    for _ in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        r1.append((x1, y1))
        r2.append((x2, y2))
        clr.append(color)
    cnt = 0
    for i in range(N):
        x1, y1 = r1[i]  # i번째 왼쪽 위 모서리
        x2, y2 = r2[i]  # i번째 오른쪽 아래 모서리
        for col in range(y1, y2+1):
            for row in range(x1, x2+1):
                if mat[col][row] == clr[i]:     # 이미 같은 값으로 색칠했다면 색칠하지 않는다.
                    pass
                else:
                    mat[col][row] += clr[i]     # 다른 색으로 색칠되어 있다면, 덧칠한다.
                    if mat[col][row] == 3:      # 덧칠한 값이 3이라면, 보라색이다.
                        cnt += 1                # 보라색 칸을 만나면, 카운트한다.

    print(f'#{Tc} {cnt}')
