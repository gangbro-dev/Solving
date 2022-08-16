import sys
sys.stdin = open('input.txt')

for Tc in range(1, 11):
    T = int(input())
    # 2차 배열 입력
    mat = [list(input()) for _ in range(100)]
    cnt = 1
    # 가로 탐색
    for column in range(100):    # 몇 번째 줄을 탐색할지
        for M in range(100, 1, -1):  # window의 크기
            # cnt보다 더 작은 window를 가지는 연산은 스킵
            if M < cnt:
                break
            for row in range(100 - M + 1):   # 몇 번째 칸의 인덱스부터 window를 시작할 지
                # 회문 탐색. 끝점부터 중앙점까지 차례로 탐색해서 모두 일치하면 정답에 복사해서 넣는다.
                for i in range(M//2):
                    if mat[column][row + i] != mat[column][row + (M-1) - i]:
                        break
                else:
                    cnt = max(M, cnt)
                    break
    # 세로 탐색
    for row in range(100):
        for M in range(100, 1, -1):
            if M < cnt:
                break
            for column in range(100 - M + 1):
                # 회문 탐색. 끝점부터 중앙점까지 차례로 탐색해서 모두 일치하면 정답에 복사해서 넣는다.
                for i in range(M // 2):
                    if mat[column + i][row] != mat[column + (M - 1) - i][row]:
                        break
                else:
                    cnt = max(M, cnt)
                    break

    print(f'#{T} {cnt}')
