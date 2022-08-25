from collections import deque

# import sys
# sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    N, M = map(int, input().split())
    q = deque(input().split())
    for _ in range(M):
        q.append(q.popleft())

    print(f'#{Tc} {q.popleft()}')
