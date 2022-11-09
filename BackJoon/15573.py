# 보자 일단 자기 강도보다 큰 값을 가져야함
# 일단 패딩 넣은 놈은 0 해줌
# 만약에 내 주변에 내 강도보다 쌘 돌만 있다면
# import sys
# input = sys.stdin.readline().rstrip

AIR_FACTOR = 1000001
N, M, K = map(int, input().split())

ores = [[0] * (M * 2)]
# 1. 좌 우 상 방향에 패딩 씌우기
for _ in range(N):
    ores.append([0] + list(map(int, input().split())) + [0])

# 그룹화?? 해보자
step_dp = [[None] * (M + 2) for _ in range(N + 1)]

for x in range(N+1):
    for y in range(M+2):
        if not ores[x][y]:
            step_dp[x][y] = 0
            continue
#         for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
#             if

print(ores)
