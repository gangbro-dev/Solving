import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    # 화물과 화물차 정리
    container.sort(reverse=True)
    truck.sort()
    # 운반시작/
    idx_t = 0
    weight = 0
    while idx_t < M:
        for mass in container:
            if mass <= truck[idx_t]:
                weight += mass
                container.remove(mass)
                break

        idx_t += 1

    print(f'#{Tc} {weight}')
