import sys
from collections import deque
sys.stdin = open('input.txt')

for Tc in range(1, 11):
    T = int(input())
    password = deque(map(int, input().split()))
    code = 1
    i = 1
    while code:
        code = password.popleft() - i
        if code < 0:
            code = 0
        password.append(code)
        i = 1 if i > 4 else i + 1

    print(f'#{T}', end=' ')
    print(*password)
