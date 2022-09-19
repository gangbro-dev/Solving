from sys import stdin
import heapq

N = int(stdin.readline())
M = int(stdin.readline())
bus = [tuple(map(int, stdin.readline().split())) for _ in range(M)]
start, end = map(int, stdin.readline().split())

adj_graph = [dict() for _ in range(N+1)]
for line in bus:
    # 노선 정보를 저장한다. 만약 자기자신으로 오는 노선이 있다면, 무시한다.
    if line[0] == line[1]:
        continue
    # 아직 저장되지 않은 노선이라면 추가한다. 겹치는 노선이라면, 비용이 작을 때, 저장한다.
    if line[1] not in adj_graph[line[0]].keys() or adj_graph[line[0]][line[1]] > line[2]:
        adj_graph[line[0]][line[1]] = line[2]

cost_table = [100001 * N] * (N+1)               # 각 노드로 가는 최소비용
cost_table[start] = 0                           # 시작점에서 시작점으로 가는 비용은 0
q = list()
heapq.heappush(q, (0, start))

while q:
    dist, now = heapq.heappop(q)
    if cost_table[now] < dist:
        continue
    # 현재 노드까지 도착하는 최소 비용 + 간선으로 인한 비용 = 이 노드에서 다음노드로 가는 비용
    for node, cost in adj_graph[now].items():
        if cost_table[now] + cost < cost_table[node]:
            cost_table[node] = cost_table[now] + cost
            heapq.heappush(q, (cost_table[node], node))

print(cost_table[end])
