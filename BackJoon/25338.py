import sys
input = sys.stdin.readline


def butt(a, b, c, d, x):
    return max(a * ((x-b)**2) + c, d)


a, b, c, d = map(int, input().split())
N = int(input())
pants = list()
ans = 0
for i in range(N):
    u, v = map(int, input().split())
    if v >= b and butt(a, b, c, d, v) == u:
        if u == d and butt(a, b, c, d, v-1) == d:
            continue
        ans += 1

print(ans)
