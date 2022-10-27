from sys import stdin

input = stdin.readline


def LCM(a, b):
    if a > b:
        L, S = a, b
    else:
        L, S = b, a
    C = -1
    while C:
        C = L % S
        L, S = S, C

    return a * b // L


N = int(input())

T = list(map(int, input().split()))
T1 = T[0]
for i in range(1, N - 2):
    T1 = LCM(T1, T[i])

print(T1)
