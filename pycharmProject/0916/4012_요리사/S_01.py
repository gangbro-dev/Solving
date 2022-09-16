import sys
sys.stdin = open('sample_input.txt')
from itertools import combinations as comb
T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    synergy = [tuple(map(int, input().split())) for _ in range(N)]
    ingredient = set(range(N))
    ans = 999999999
    for a in comb(ingredient, N//2):
        A = set(a)
        B = ingredient - A
        # A 시너지 구하기
        s_a = 0
        for x in A:
            for y in A:
                s_a += synergy[x][y]
        # B 시너지 구하기
        s_b = 0
        for x in B:
            for y in B:
                s_b += synergy[x][y]
        # 시너지 차 구하기
        ans = min(abs(s_a - s_b), ans)

    print(f'#{Tc} {ans}')
