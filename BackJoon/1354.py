N, P, Q, X, Y = map(int, input().split())

A = [0] * 1000001
A[0] = 1
for i in range(1, 1000001):
    AA = (i // P) - X
    BB = (i // Q) - Y
    A[i] = A[0 if AA < 0 else AA] + A[0 if BB < 0 else BB]

lst = [N]
ans = 0
while lst:
    i = lst.pop()
    if i < len(A):
        ans += A[i]
        continue
    AA = (i // P) - X
    BB = (i // Q) - Y
    lst.append(0 if AA < 0 else AA)
    lst.append(0 if BB < 0 else BB)

print(ans)
