N = int(input())
to_1 = [0, 0]
for i in range(2,N+1):
    to_1.append(to_1[i-1]+1)
    if not i % 2:
        to_1[i] = min(to_1[i//2] +1, to_1[i])
    if not i % 3:
        to_1[i] = min(to_1[i//3] +1, to_1[i])

print(to_1[N])