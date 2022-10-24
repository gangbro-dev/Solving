def sol(N, P, Q):
    global DP
    if N not in DP.keys():
        DP[N] = sol(N//P, P, Q) + sol(N//Q, P, Q)
    return DP[N]

N, P, Q = map(int, input().split())

DP = dict([(0, 1), (1, 2)])
lst = [N]
ans = sol(N, P, Q)

print(ans)
