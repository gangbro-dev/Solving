n, k = map(int, input().split())
coin = []                           # 동전 배열
dp = [0] * (k+1)                       # dp 리스트
# 동전 입력
for _ in range(n):
    coin.append(int(input()))
    if coin[-1] <= k:
        dp[coin[-1]] = 1
# 동전을 최대한 적게 써야한다 -> 큰 동전 먼저 써야한다.
coin.sort(reverse=True)
# 모든 동전에 대해서 실행 -> 소팅 필요한가? -> 하는게 빠르네
for penny in coin:
    for idx in range(penny, k):
        # 인덱스에 동전조합이 존재하고, k 이하인 값에 대해서
        if dp[idx] and idx + penny <= k:
            # 계산한 값에 개수가 존재하지 않으면, 대입
            if not dp[idx + penny]:
                dp[idx + penny] = dp[idx] + 1
            # 존재하는 값이 지금 계산된 값보다 크면, 대입
            elif dp[idx + penny] > dp[idx] + 1:
                dp[idx + penny] = dp[idx] + 1

if dp[k]:
    print(dp[k])
else:
    print(-1)
