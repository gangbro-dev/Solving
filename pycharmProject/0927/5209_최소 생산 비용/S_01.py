import sys
sys.stdin = open('sample_input.txt')


def min_cost(N, cost, now_C, per, order):
    global min_C
    if len(per) < N:
        for idx in range(N):
            if min_C > now_C and idx not in per:
                temp = now_C + cost[order][idx]
                min_cost(N, cost, temp, per + [idx], order + 1)
    else:
        min_C = min(min_C, now_C)


T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    min_C = 999999999999999
    min_cost(N, cost, 0, list(), 0)

    print(f'#{Tc} {min_C}')
