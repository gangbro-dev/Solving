# RGB 1
# N = int(input())
#
# cost = list()
# for _ in range(N):
#     cost.append(list(map(int, input().split())))
# DP = list()
# DP.append(cost[0])
#
# for i in range(1, N):
#     DP.append([0] * 3)
#     for j in range(3):
#         A = (j + 1) % 3
#         B = (j + 2) % 3
#         DP[i][j] = min(DP[i-1][A], DP[i-1][B]) + cost[i][j]
#
# print(min(DP[-1]))

# RGB1 과 다른점 = 마지막 칸이 첫 칸과 달라야 한다. -> 마지막 선택에 체크 만들어서 체크후 제출
# => 실패. 최소값만 찾아가니 마지막 값이 너무 큰 경우 실패
# 2개 만들어서 해볼까?

import sys

input = sys.stdin.readline

N = int(input())

cost = list()
for _ in range(N):
    cost.append(list(map(int, input().split())))
DP = list()
first = list()
for i in range(3):
    first.append((cost[0][i], i))
DP.append(first)

for i in range(1, N - 1):
    DP.append([0] * 3)
    for j in range(3):
        A = (j + 1) % 3
        B = (j + 2) % 3
        if DP[i - 1][A][0] == DP[i - 1][B][0]:
            if DP[i - 1][A][1] != DP[i - 1][B][1]:
                DP[i][j] = DP[i - 1][A][0] + cost[i][j], 3
            else:
                DP[i][j] = DP[i - 1][A][0] + cost[i][j], A
        elif DP[i - 1][A][0] < DP[i - 1][B][0]:
            DP[i][j] = DP[i - 1][A][0] + cost[i][j], A
        else:
            DP[i][j] = DP[i - 1][B][0] + cost[i][j], B
else:
    DP.append([N * 1000] * 3)
    # 마지막 칸 채우기 => 앞 뒤를 확인해야 한다.
    # 현재 채우고자 하는 칸
    for x in range(3):
        # 선택할 수 있는지 없는 지 확인할 이전 칸
        for y in range(3):
            # 이전 값과 이후 값이 현재 값과 같은 색깔이면 스킵
            if DP[-2][y][1] == 3:
                pass
            elif x == y or x == DP[-2][y][1]:
                continue
            # 아니라면 선택할 수 있는 최소값을 선택한다.
            DP[-1][x] = min(DP[-1][x], DP[-2][y][0] + cost[-1][x])

print(min(DP[-1]))
