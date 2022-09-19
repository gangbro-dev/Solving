import sys
from collections import deque
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    E, N = map(int, input().split())
    adj_graph1 = [0] * (E + 2)
    adj_graph2 = [0] * (E + 2)
    data = map(int, input().split())
    for _ in range(E):
        p, c, *data = data
        if adj_graph1[p]:
            adj_graph2[p] = c
        else:
            adj_graph1[p] = c

    q = deque()
    q.append(N)
    cnt = 1
    while q:
        node = q.popleft()
        if adj_graph1[node]:
            q.append(adj_graph1[node])
            cnt += 1
            if adj_graph2[node]:
                q.append(adj_graph2[node])
                cnt += 1

    print(f'#{Tc} {cnt}')
