from collections import deque
import sys
sys.stdin = open('sample_input.txt')

def rotate_oven(oven_size, pizza_queue):
    q = deque([0] * oven_size)
    served_pizza = []
    i = 1
    while q:
        while pizza_queue:
            oven_hole = q.popleft()
            if not oven_hole:
                q.append([pizza_queue.popleft(), i])
                i += 1
            else:
                melt_pizza = [oven_hole[0] // 2, oven_hole[1]]
                if melt_pizza[0]:
                    q.append(melt_pizza)
                else:
                    served_pizza.append(melt_pizza[1])
                    q.append([pizza_queue.popleft(), i])
                    i += 1

        melt_pizza = q.popleft()
        melt_pizza = [melt_pizza[0] // 2, melt_pizza[1]]
        if melt_pizza[0]:
            q.append(melt_pizza)
        else:
            served_pizza.append(melt_pizza[1])
    return served_pizza


T = int(input())

for Tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza_queue = deque(map(int, input().split()))

    print(f'#{Tc} {rotate_oven(N, pizza_queue)[-1]}')
