import sys
sys.stdin = open('sample_input.txt')

T = int(input())
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for Tc in range(1, T+1):
    N = int(input())
    # 입력받는 2차원 배열에 패딩을 씌워서 인덱스에러를 방지한다.
    mat = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    mat = [[0] * (N+2)] + mat + [[0] * (N+2)]
    # 부모(인덱스)-자식(원소)간 트리 구조를 저장할 리스트를 작성한다 크기는 N**2 + 1
    # 만약 부모(작은 값)에서 자식(큰값)이 인접하다면, True, 아니라면 False를 저장
    ch = [False] * ((N ** 2) + 1)
    for x in range(1, N+1):
        for y in range(1, N+1):
            for dx, dy in delta:
                if mat[x][y] + 1 == mat[x + dx][y + dy]:
                    ch[mat[x][y]] = True
    # 이어지는 개수를 카운트. True라면, 간선이 존재한다는 뜻이고, 이는 길이가 2라는 뜻이므로 초기값은 1
    cnt = 1
    ans = 0             # 총 이어진 길이중 최대길이
    start = 0           # 최대길이의 출발점
    for i in range(1, len(ch)):
        if ch[i]:
            if not ch[i-1]:     # 이전 값이 False인 값이면, 출발점이므로 저장
                temp = i
            cnt += 1
            if cnt > ans:       # 출발점으로부터의 길이가 가장 길다면, 그 출발점과 길이 저장
                ans = cnt
                start = temp
        else:
            cnt = 1

    print(f'#{Tc} {start} {ans}')
