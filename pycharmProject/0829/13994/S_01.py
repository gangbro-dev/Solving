import sys
sys.stdin = open('sample_in.txt')

T = int(input())

for Tc in range(1, T+1):
    bus_stop = [0] * 1001
    N = int(input())
    for bus in range(N):
        bus_type, A, B = map(int, input().split())
        if bus_type == 1:
            for stop in range(A, B+1):
                bus_stop[stop] += 1
        elif bus_type == 2:
            bus_stop[A] += 1
            bus_stop[B] += 1
            for stop in range(A + 2, B, 2):
                bus_stop[stop] += 1
        elif bus_type == 3:
            bus_stop[A] += 1
            bus_stop[B] += 1
            if A % 2:
                for stop in range(A+1, B):
                    if not stop % 3 and stop % 10:
                        bus_stop[stop] += 1
            else:
                for stop in range(A + 1, B):
                    if not stop % 4:
                        bus_stop[stop] += 1

    print(f'#{Tc} {max(bus_stop)}')
