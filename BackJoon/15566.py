def frogSetting(N, K, frog, favleaf, state, idx=1):
    for favleaf in favleaf[idx]:
        next_state = state[:]
        next_state[favleaf] = idx
        # 주변 개구리 보자
        for otherfrog in adjLog[favleaf]:
            if state[otherfrog]:
                for i in range(4):
                    if frog[otherfrog][i] ==

N, M = map(int, input())
frog = list((None,))
favleaf = [None] * (N+1)
adjLog = [] * (N+1)
for i in range(N):
    frog.append(tuple(map(int, input().split())))

for i in range(1, N+1):
    A, B = map(int, input().split())
    if A == B:
        favleaf[i] = (A,)
    else:
        favleaf[i] = (A, B)


for i in range(M):
    A, B, T = map(int, input().split())
    adjLog[A].append((B, T-1))
    adjLog[B].append((A, T-1))

state = [None] * N + 1
frogSetting(N, K, frog, favleaf, state)