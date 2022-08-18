T = int(input())

for Tc in range(1,T+1):
    N = int(input())
    pascal = [[1]]
    for i in range(1, N):
        pascal.append([])
        pascal[i].append(1)
        if i == 1:
            pascal[i].append(1)
        elif i > 1:
            for j in range(1, i):
                pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
            else:
                pascal[i].append(1)

    print(f'#{Tc}')
    for _ in range(N):
        print(*pascal[_])