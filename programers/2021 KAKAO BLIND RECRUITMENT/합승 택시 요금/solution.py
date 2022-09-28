def solution(n, s, a, b, fares):
    INF = int(1e9)

    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        graph[i][i] = 0

    for fare in fares:
        graph[fare[0]][fare[1]] = fare[2]
        graph[fare[1]][fare[0]] = fare[2]

    for k in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

    answer = INF
    for k in range(1, n + 1):
        answer = min(graph[s][k] + graph[k][a] + graph[k][b], answer)

    return answer
