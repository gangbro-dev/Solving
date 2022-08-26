import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    print(f'#{Tc}', end=' ')
    cost = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    plan_cost = [0] * 12
    # 달 별로 한달권 vs 일일권 다수
    for month in range(len(plan)):
        if plan[month] * cost[0] <= cost[1]:
            plan_cost[month] = plan[month] * cost[0]
        else:
            plan_cost[month] = cost[1]
    plan3_cost = [0] * (12 - 3 + 1)
    # 달별 최솟값 vs 3달권
    for month3 in range(10):
        if sum(plan_cost[month3:month3+3]) > cost[2]:
            plan3_cost[month3] = 1
    # 3달권 이득인 구간이 존재할 때
    if 1 in plan3_cost:
        # 3달권 이득인 구간이 딱 3의 배수인 경우
        if (sum(plan3_cost)-1) % 3 == 0:
            i = 0
            while i < 10:
                if plan3_cost[i]:
                    plan_cost[i] = cost[2]
                    plan_cost[i+1] = 0
                    plan_cost[i+2] = 0
                    i += 3
                else:
                    i += 3
        # 3달권 이득인 구간이 3의 배수가 아닌경우
        else:
            # 가장 작은 나머지 값을 찾아서 3달권보다 싸다면 포함 구간 제거
            x = (sum(plan3_cost) - 1) % 3
            sorted_cost = sorted(plan_cost, reverse=True)
            while not sorted_cost[-1]:
                sorted_cost.pop()
            for i in range(x):
                a = plan_cost.index(sorted_cost.pop())
                if plan_cost[a] < cost[2]:
                    if a == 11:
                        plan3_cost[-1] = 0
                    elif a == 10:
                        plan3_cost[-1] = 0
                        plan3_cost[-2] = 0
                    else:
                        plan3_cost[a] = 0
                        plan3_cost[a-1] = 0
                        plan3_cost[a-2] = 0
            # 3달권이 이득인 구간은 3달권으로 변경
            i = 0
            while i < 10:
                if plan3_cost[i]:
                    plan_cost[i] = cost[2]
                    plan_cost[i + 1] = 0
                    plan_cost[i + 2] = 0
                    i += 3
                else:
                    i += 3

    print(min(cost[3], sum(plan_cost)))
