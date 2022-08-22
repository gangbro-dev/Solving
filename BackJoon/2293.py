# 전체 코인들은 큰 수, 작은 수 가 나눠져 있을 것.
# 전체 코인들을 가장 적은 개수로 합을 표현할 수 있는 방법을 찾는다.
# 그 방법에서 가장 큰 코인을 가장 적은 개수로 나머지 숫자로 표현할 수 있는 방법을 찾는다
# 각각의 코인들에 위와 같은 방법을 사용해서 나누어 표현하면
# 곱셈을 통해서 총 가짓 수를 알 수 있을 것이다. -> 반례확인 폐기
# def smallist_set(value, coin_list):
#     count = [0] * len(coin_list)
#     i = len(coin_list) - 1
#     while value > 0:
#         value -= coin_list[i]
#         if value >= 0:
#             count[i] += 1
#         else:
#             value += coin_list[i]
#             count[i] -= 1
#             i -= 1
#     else:
#         return count
#     return 0
#
#
# divide_coin = [1] * n
# ';'
# for i in range(1, n):
#     value = coin[i]
#     smaller_coin = coin[:i]
#     smaller_set = smallist_set(value, smaller_coin)
#     for  in smaller_set:
#         [i] = divide_coin[]
#
# dp를 빈 리스트의 리스트로 만들어서
# 가장 작은 동전부터 각 동전에 맞는 가치를 가진 인덱스에
# 각 동전만 들어간 리스트를 추가한다.
# 이제 가장 작은 동전 인덱스부터 거기 있는 모든 리스트에 각 동전을 추가한 리스트를 만들고,
# 그 리스트가 가진 동전의 합의 인덱스에 그 리스트를 추가한다.
# 이때, 목표값 k를 넘는 크기를 가지는 리스트가 나오면 추가할 수 없으므로 스킵
# 이렇게 인덱스를 하나씩 올려가며 반복하게 되면 최종적으로
# k값을 표현할 수 있는 모든 리스트가 k 인덱스 내에 있게되고,
# 그 개수를 출력하면 된다.
# -> 메모리 폭파
# 아마도 dp가 메모리를 너무 많이 잡아먹는듯?
# dp 이전 값들을 모두 지우면 괜찮지 않을까 -> 실패
# n, k = map(int, input().split())
# coin = []
# dp = [[] for _ in range(k+1)]
# for _ in range(n):
#     coin.append(int(input()))
#     dp[coin[-1]].append([coin[-1]])
#
# coin.sort()
# idx = coin[0]
#
# while idx < k:
#     if dp[idx]:
#         for i in dp[idx]:
#             for penny in coin:
#                 if sum(i) + penny <= k:
#                     temp = sorted(i[:] + [penny])
#                     if temp not in dp[sum(i) + penny]:
#                         dp[sum(i) + penny].append(temp)
#     dp[idx].clear()
#     idx += 1
#
# print(len(dp[k]))
#
# 백준 첫번째 예시에서 1, 2, 5 코인으로 10을 표현하는 모든 조합을 찾았다.
# 가능한 경우를 모두 써보았다.
# 1로만 이루어진 집합 => 1개
# 1, 2로 이루어진 집합 => k//2개 + 1개
# 1, 2, 5로 이루어진 집합 => (k-5)번째 있는 가격을 만든 집합의 개수 -> 얘만 뭔가 명확한 규칙이 있음
# 흠.... 작은 순서대로 코인을 쓴 것을 카운트하면 될까?
# 1 -> 1개
# 2 -> p(k-2)
# 5 -> p(k-5)
# 시발 찾았다
n, k = map(int, input().split())
coin = []

for _ in range(n):
    coin.append(int(input()))

dp = [0] * (k + 1)
dp[0] = 1

coin.sort()

for penny in coin:
    idx = penny
    while idx <= k:
        dp[idx] += dp[idx-penny]
        idx += 1

print(dp[k])
