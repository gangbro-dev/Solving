import sys
sys.stdin = open('input.txt')

T = int(input())

for Tc in range(1, T+1):
    P, A, B = map(int, input().split())
    cntA = 0                # 탐색 횟수 체크
    cntB = 0
    winA = True            # 탐색 완료 체크
    winB = True
    la, lb = 1, 1
    ra, rb = P, P
    while winA and winB: # A 또는 B가 완료했다면
        # A 행동
        ca = (la + ra) // 2
        if ca == A:         # 목표에 도달한다면,
            winA = False     # A가 완료했다는 체크
        else:               # 아니라면, 이진 탐색을 위해서 끝점을 조작
            if ca > A:
                ra = ca
            else:
                la = ca
            cntA += 1       # 이진탐색한 횟수 체크

        # B 행동
        cb = (lb + rb) // 2

        if cb == B:         # 목표에 도달한다면,
            winB = False     # B가 완료했다는 체크
        else:               # 아니라면, 이진 탐색을 위해서 끝점을 조작
            if cb > B:
                rb = cb
            else:
                lb = cb
            cntB += 1       # 이진탐색한 횟수 체크

    if cntA == cntB:        # 이진 탐색한 횟수가 같다면,
        result = 0
    elif cntA > cntB:       # A 가 더 오래 탐색했다면,
        result = 'B'
    else:                   # B 가 더 오래 탐색했다면,
        result = 'A'

    print(f'#{Tc} {result}')
