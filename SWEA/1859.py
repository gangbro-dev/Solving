import sys
sys.stdin = open('input.txt')

T = int(input())

for Tc in range(1, T+1):
    day = int(input())
    cost = []
    cost.extend(map(int, input().split()))
    cost = cost[::-1]
    buy = []
    profit = 0
    max_price = max(cost)
    for i in range(len(cost)):
        price = cost.pop()
        if price == max_price:
            for j in buy:
                profit += price - j
            buy.clear()
            if cost:
                max_price = max(cost)
        else:
            buy.append(price)

    print(f'#{Tc} {profit}')
