from collections import deque
T = int(input())

for Tc in range(T):
    p = input()
    n = int(input())
    arr = deque()
    temp = input().strip('[]')
    if temp:
        arr.extend(temp.split(','))
    pop_front = True
    for func in p:
        if func == 'D' and not arr:
            print('error')
            break
        elif func == 'D':
            if pop_front:
                arr.popleft()
            else:
                arr.pop()
        elif func == 'R':
            pop_front = not pop_front
    else:
        if pop_front:
            print('[', end='')
            print(*arr, sep=',', end='')
            print(']')
        else:
            print('[', end='')
            arr.reverse()
            print(*arr, sep=',', end='')
            print(']')
