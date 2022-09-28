import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    day, month, mon3, year = map(int, input().split())
    swim_cost = list(map(int, input().split()))
    # 0. 일할계산
    for idx in range(len(swim_cost)):
        swim_cost[idx] = swim_cost[idx] * day
    # 1. 월별 일할 계산 > 한달권
    for idx_mon in range(len(swim_cost)):
        if swim_cost[idx_mon] > month:
            swim_cost[idx_mon] = month
    # 2. 한달권 * 3 > 3달권
    flag = True
    mon3_total = 0
    while flag:
        flag = False
        max_value = 0
        max_mon3 = 0
        for idx_mon3 in range(len(swim_cost)-2):
            if swim_cost[idx_mon3] + swim_cost[idx_mon3 + 1] + swim_cost[idx_mon3 + 2] > max_value:
                max_value = swim_cost[idx_mon3] + swim_cost[idx_mon3 + 1] + swim_cost[idx_mon3 + 2]
                max_mon3 = idx_mon3
        if max_value > mon3:
            flag = True
            del swim_cost[max_mon3]
            del swim_cost[max_mon3]
            del swim_cost[max_mon3]
            mon3_total += mon3
    # 1년 이용권
    y = sum(swim_cost) + mon3_total
    if y > year:
        print(f'#{Tc} {year}')
    else:
        print(f'#{Tc} {y}')
