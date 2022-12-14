import sys

input = sys.stdin.readline

N = int(input())

cost = list()
for _ in range(N):
    cost.append(list(map(int, input().split())))
result = list()
result.append(cost[0])

for i in range(1, N):
    result.append([0] * 3)
    for j in range(3):
        A = (j + 1) % 3
        B = (j + 2) % 3
        result[i][j] = min(result[i-1][A], result[i-1][B]) + cost[i][j]

print(min(result[-1]))
