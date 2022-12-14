import sys

input = sys.stdin.readline

N = int(input())
town = list(map(int, input().split()))
adj = dict()
for i in range(N):
    adj[i] = [town[i], []]
# N개의 노드가 모두 연결된 N-1 개의 간선 => 최소신장트리
for i in range(N-1):
    a, b = map(int, input().split())
    adj[a][1].append(b)
    adj[b][1].append(a)

sorted_town = sorted(adj, key=lambda x:x[0])
# max값 포함과 미포함을 나눠서 결과값을 도출해볼까?
for t in sorted_town:


