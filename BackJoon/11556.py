def setting_frog(Frog, Favleaf, Adjlog, frognum):
    if frognum

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

