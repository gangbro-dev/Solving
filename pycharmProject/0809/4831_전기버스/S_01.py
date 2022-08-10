# 한칸씩 가면서 가장 최근에 지나친 충전소 위치를 기억해 놨다가,
# 배터리가 다 닳았을 때, 충전했엇지 라고 가정하고, 배터리양을 다시 계산한다.

import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for x in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge_M = list(map(int, input().split()))
    # 오류 방지용 추가 항
    charge_M.append(-1)

    now = 1  # 현재 위치 now
    LS = 0  # 충전소 인덱스
    count = 0  # 충전한 횟수
    battery = K  # 현재 배터리 양
    charge_stop = 0  # 직전에 있었던 충전소 위치

    while now < N:
        battery -= 1

        # 지나간 마지막 충전소 위치를저장
        if charge_M[LS] == now:
            charge_stop = now
            LS += 1
        # 배터리가 다 닳았을때, 직전의 정류장에서 충전한 척 하기
        if battery == 0:
            # 직전의 정류장에서 충전해서 지금 위치까지 왔을때, 남아있을 배터리 양
            battery = K - (now - charge_stop)
            # 충전한 횟수 추가
            count += 1

        if battery <= 0:
            count = 0
            break

        now += 1

    print(f'#{x} {count}')