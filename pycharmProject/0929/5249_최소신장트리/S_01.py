import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_dict = dict()
    visited = [False] * (V + 1)
    for i in range(1, V+1):
        adj_dict[i] = []
    for _ in range(E):
        a, b, c = map(int, input().split())
        adj_dict[a].append((b, c))
        adj_dict[b].append((a, c))
    lines = adj_dict[1][:]
    while lines:
        

    print(f'#{Tc} {}')
