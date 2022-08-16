import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    N, M = map(int, input().split())
    mat = []
    ans = '' # 정답 문자열
    for i in range(N):
        temp = input()
        mat.append([])
        for j in temp:
            mat[i].append(j)
    # 가로 탐색
    for column in range(N):
        for row in range(N-M+1):
            # 회문 탐색. 끝점부터 중앙점까지 차례로 탐색해서 모두 일치하면 정답에 복사해서 넣는다.
            for i in range(M//2):
                if mat[column][row+i] != mat[column][row+M-1-i]:
                    break
            else:
                for i in range(M):
                    ans += mat[column][row+i]
                break
        # 정답을 찾은 경우 반복 중지
        if ans:
            break

    # 가로 탐색이 성공한 경우 세로 탐색 안함
    if ans:
        pass
    else:
        # 세로 탐색
        for row in range(N):
            for column in range(N - M + 1):
                # 회문 탐색. 끝점부터 중앙점까지 차례로 탐색해서 모두 일치하면 정답에 복사해서 넣는다.
                for i in range(M//2):
                    if mat[column+i][row] != mat[column+M-1-i][row]:
                        break
                else:
                    for i in range(M):
                        ans += mat[column+i][row]
                    break
            # 정답을 찾은 경우 반복 중지
            if ans:
                break
    print(f'#{Tc} {ans}')
