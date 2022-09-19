import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    N, M, L = map(int, input().split())
    binary_tree = [0] * (N+1)
    for _ in range(M):
        node, value = map(int, input().split())
        binary_tree[node] = value

    for i in range(N, 1, -1):
        binary_tree[i//2] += binary_tree[i]

    print(f'#{Tc} {binary_tree[L]}')
