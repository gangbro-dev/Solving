from collections import deque
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = {}
    for _ in range(E):
        a, b = map(int, input().split())
        if a not in graph.keys():
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph.keys():
            graph[b] = [a]
        else:
            graph[b].append(a)

    S, G = map(int, input().split())
    visited = [0] * (V + 1)
    q = deque([S])
    ans = 0
    while q:
        node = q.popleft()
        if node == G:
            ans = visited[node]
            break
        for next_node in graph[node]:
            if not visited[next_node]:
                q.append(next_node)
                visited[next_node] = visited[node] + 1
    else:
        ans = 0

    print(f'#{Tc} {ans}')
