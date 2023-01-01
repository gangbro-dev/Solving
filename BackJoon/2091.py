from sys import stdin

input = stdin.readline

X, *MAX_COIN = map(int, input().split())
# (*사용한 동전 수[a, b, c, d])
DP = [[0] * 4 for _ in range(X + 1)]
coin = [1, 5, 10, 25]

for c in range(4):
    if coin[c] <= X and MAX_COIN[c]:
        DP[coin[c]][c] += 1

for i in range(1, X):
    # Y + Z 원을 표시하려면 Y원에서 Z원짜리 동전을 하나 더 쓰는법이 있음
    # 조건1. Y + Z원이 X원보다 작은 값인지 (큰 값이면 알 필요 없음)
    # 조건2. Z원 동전이 남았는지 확인
    # 조건3. 지금 Z원 동전을 하나 더 쓰는 방법이 이전 방법보다 더 동전을 많이 사용하고 있는지
    # 위의 조건을 만족하면 새로운 동전 사용법을 갱신
    if not sum(DP[i]):
        continue
    for c in range(3, -1, -1):
        if i + coin[c] <= X and DP[i][c] < MAX_COIN[c] and sum(DP[i + coin[c]]) < sum(DP[i]) + 1:
            DP[i + coin[c]] = list(DP[i])
            DP[i + coin[c]][c] += 1

print(*DP[-1])

# 112 4 10 4 2