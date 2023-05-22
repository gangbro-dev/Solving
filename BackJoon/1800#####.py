from sys import stdin
import heapq

# 1번과 N번 컴퓨터를 연결하는 최소의 비용을 가지는 경로
# 처음부터 K 개의 결선에는 가격을 책정하지 않음(리스트로 가격 값만 가지고 감)
# K 개가 넘어가게 되면, 최대값 K+1개만 저장하며 가져감

input = stdin.readline
N, P, K = map(int, input().split())
# 연결 그래프를 표시할 딕셔너리
net = dict()

for _ in range(P):
    A, B, COST = map(int, input().split())
    # A -> B 연결 표현
    if A in net.keys():
        net[A].append((B, COST))
    else:
        net[A] = [(B, COST)]
    # B -> A 연결 표현
    if B in net.keys():
        net[B].append((A, COST))
    else:
        net[B] = [(A, COST)]

# BFS를 툥해서 1번에서 N번까지 이어진 방법들 중 가장 적은 가격으로 연결할 수 있는 방법 표시
# 최대값 K+1 개를 가지고 가는 방법 (최소힙 사용)
# [0, 0, 0, 0, 0] 의 최소 힙을 기본으로 사용
# 가격이 들어오면 우선 heappop 해서 크기 비교 후 더 큰 값을 다시 heappush
# N 번에 도달하면, heap의 최소값(0번 인덱스)가 정답임

cost = [0] * (K + 1)
