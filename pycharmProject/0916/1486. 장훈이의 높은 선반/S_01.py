# import sys
# sys.stdin = open('input.txt')
from itertools import combinations as comb
T = int(input())

for Tc in range(1, T+1):
    N, B = map(int, input().split())
    height = tuple(map(int, input().split()))

    answer = 20 * 10001
    for n in range(1, N + 1):
        for tower in comb(height, n):
            if B <= sum(tower) < answer:
                answer = sum(tower)

    print(f'#{Tc} {answer - B}')
