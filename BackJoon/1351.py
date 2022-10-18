N, P, Q = map(int, input().split())

A = [0] * 1000001
A[0] = 1
for i in range(1, 1000001):
    A[i] = A[i//P] + A[i//Q]

lst = [N]
ans = 0
while lst:
    i = lst.pop()
    if i < len(A):
        ans += A[i]
        continue
    lst.append(i//P)
    lst.append(i//Q)

print(ans)
