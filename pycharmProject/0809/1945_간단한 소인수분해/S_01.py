import sys
sys.stdin = open('input.txt')

T = int(input())

for x in range(1, T+1):
    N = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    while not (N % 2):
        N //= 2
        a += 1
    while not (N % 3):
        N //= 3
        b += 1
    while not (N % 5):
        N //= 5
        c += 1
    while not (N % 7):
        N //= 7
        d += 1
    while not (N % 11):
        N //= 11
        e += 1
    print(f'#{x} {a} {b} {c} {d} {e}')
