import sys
from collections import deque
sys.stdin = open('input.txt')


T = int(input())

for Tc in range(1, T+1):
    N, K = map(int, input().split())
    way = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    visited[0] = True
    for i in range(K):
        graph[way[2 * i]].append(way[2 * i+1])
        graph[way[2 * i + 1]].append(way[2 * i])

    ans = []
    q = deque()
    q.append(1)
    visited[1] = True
    while q:
        point = q.popleft()

        ans.append(point)
        for next in graph[point]:
            if not visited[next]:
                q.append(next)
                visited[next] = True

    print(f'#{Tc}', end=' ')
    print(*ans)
