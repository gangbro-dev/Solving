import sys
sys.stdin = open('input.txt')


def workeffi(P, NP, N, per, order):
    global max_P
    if len(per) < N:
        for idx in range(N):
            if max_P <= NP and NP and idx not in per:
                NNP = NP * (P[order][idx] / 100)
                workeffi(P, NNP, N, per + [idx], order + 1)
    else:
        max_P = max(NP, max_P)

    return max_P


T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    max_P = 0
    ans = round(workeffi(P, 1, N, [], 0)*100, 6)
    print(f'#{Tc} {ans:.6f}')
