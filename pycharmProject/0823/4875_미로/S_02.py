import sys
sys.stdin = open('sample_input.txt')

T = int(input())  # 테스트 개수
for i in range(1, T + 1):  # 테스트 번호
    N = int(input())  # 배열 길이
    M = [list(map(int, input())) for _ in range(N)]  # 미로 모양
    result = 0  # 결과값 초기
    x = [1, -1, 0, 0]  # x방향
    y = [0, 0, 1, -1]  # y방향
    for j in range(N):
        for k in range(N):  # 미로 안에서
            if M[j][k] == 2:  # 출발점 찾으면
                stack = [(j, k)]  # 스택에 넣기
    while stack:  # 스택 안에 아무것도 없을 때까지
        X, Y = stack.pop()  # 출발지 지우기
        M[X][Y] = 1  # 간 곳은 1로 벽 세우기
        for l in range(4):  # 방향전환
            dx = X + x[l]  # x바꾸기
            dy = Y + y[l]  # y바꾸기
            if dx < 0 or dy < 0 or dx >= N or dy >= N:  # 미로에서 벗어나면
                continue  # 다른 방향으로 바꾸기
            if M[dx][dy] == 3:  # 도착하면
                result = 1  # 결과값 1로 바꾸기
                break  # 끝
            elif M[dx][dy] == 0:  # 갈림길에서
                stack.append((dx, dy))  # 빈공간 다 스택에 저장

        # break  # 도착하면 나머지 길은 확인필요X
    print(f'#{i} {result}')
