from sys import stdin

input = stdin.readline

N = int(input())

matrix_num = list(map(int, input().split()))
for i in range(1, N):
    matrix_num.append(int(input().split()[-1]))
# 행렬 곱 중 최솟값을 구하여서 그 행렬곱을 수행하고, 나머지 행렬들에 대해서 반복 => 실패
# ans = 0
# while len(matrix_num) > 2:
#     temp = 999999999999
#     idx = len(matrix_num)
#     for i in range(1, len(matrix_num) - 1):
#         product = matrix_num[i-1] * matrix_num[i] * matrix_num[i+1]
#         if temp > product:
#             temp = product
#             idx = i
#     ans += temp
#     matrix_num.pop(idx)
#
# print(ans)
# n * m * k 를 이용해서 DP를 만들어보자자
INF = 500 ** 3
DP = [[INF] * N for _ in range(N)]
# 1. 가장 작은 구간의 값들을 구함 => n * m * k
# 2. 하나 더 큰 구간들의 값을 구함 -> 이때, 구간을 두개로 나눠서 각각의 연산횟수 합들 + 두 구간곱의 곱연산 횟수
# 3. 시작점 n, 중간점 m, 끝점 k를 알면 나머지는 이미 계산한 연산횟수 합만 더하면 됨
for l in range(N):   # (1 ~ N 까지) 구간의 크기
    for n in range(N - l):  # 시작점
        k = l + n   # 끝점 - 1
        if n == k:
            DP[n][k] = 0    # 시작점 끝점 같음 => 그냥 2*2 행렬이란 뜻

        for m in range(n, k):   # 중간점
            DP[n][k] = min(DP[n][k], DP[n][m] + DP[m+1][k] + matrix_num[n]*matrix_num[m+1]*matrix_num[k+1])

print(DP[0][N-1])


