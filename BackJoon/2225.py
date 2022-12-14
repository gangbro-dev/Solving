def 경우의수(n, k, DP):
    if DP[n][k]:
        return DP[n][k]
    ans = 0
    for i in range(n + 1):
        if DP[i][k - 1]:
            ans += DP[i][k - 1]
        else:
            ans += 경우의수(i, k - 1, DP)
    DP[n][k] = ans
    return ans


N, K = map(int, input().split())
DP = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(len(DP[0])):
    DP[0][i] = 1
for i in range(len(DP)):
    DP[i][1] = 1
print(경우의수(N, K, DP) % 1000000000)
