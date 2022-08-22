n, k = map(int, input().split())
coin = []
dp = [[] for _ in range(k+1)]
for _ in range(n):
    coin.append(int(input()))
    dp[coin[-1]].append([coin[-1]])

coin.sort()
idx = coin[0]
for penny in coin:
    while idx < k:
        dp =
        idx += 1

print(len(dp[k]))