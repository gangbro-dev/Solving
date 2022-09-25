import sys
from itertools import permutations
sys.stdin = open('sample_input.txt')
input = sys.stdin.readline

T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    min_cost = 100 * N
    for way in permutations(range(1, N)):
        way = [0] + list(way) + [0]
        cost_sum = 0
        for i in range(N):
            cost_sum += cost[way[i]][way[i+1]]
            if min_cost < cost_sum:
                break
        else:
            min_cost = cost_sum

    print(f'#{Tc} {min_cost}')
