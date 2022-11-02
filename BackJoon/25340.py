import sys

input = sys.stdin.readline

TC = int(input())
for tc in range(1, TC + 1):
    N, T = map(int, input().split())
    signals = []
    for i in range(N):
        signals.append(tuple(map(int, input().split())))
    Elist = list(map(int, input().split()))
    # 역순으로 구해보자
    # 1. 도착한 순간 T초가 아니라면 할 수 없음.
    # 도착시간 = 마지막 신호등의 도착할 수 있는 마지막 주기 + 선린랜드까지의 시간
    A, B, C, D = signals.pop()
    E = Elist.pop()
    # 아래 if식에서 통과하지 못한다면 애초에 도착할 수 있는 주기가 존재하지 않음
    lt = (T - C - E) % A
    if lt > B - D:
        print(no)
        continue
    else:
        T -= E + D
    # 이제 역추적하자. 역산한 출발시간이 역수라면, 불가능
    while signals:
        if T < 0:
            break
        A, B, C, D = signals.pop()
        E = Elist.pop()
        if (T - C - E) % A > B - D:
            T -=
        pass
    else:
        print(yes)
        continue
    print(no)