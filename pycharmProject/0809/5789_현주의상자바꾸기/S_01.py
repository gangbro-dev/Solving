import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for x in range(1, T+1):
    N, Q= map(int, input().split())
    Box = [0]*N
    L = [0]
    R = [0]

    for i in range(Q):
        temp = tuple(map(int, input().split()))
        L.append(temp[0])
        R.append(temp[1])

    for i in range(1, Q+1):
        for j in range(L[i], R[i] + 1):
            Box[j-1] = i

    print(f'#{x}', end=' ')
    for i in range(N):
        print(f'{Box[i]}', end=' ')
    print()
