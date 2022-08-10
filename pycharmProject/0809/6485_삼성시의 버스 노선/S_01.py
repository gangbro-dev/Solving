import sys
sys.stdin = open('s_input.txt')

T = int(input())
Bus_stop = [0]*5001
for x in range(1, T+1):
    N = int(input())
    A = []
    B = []

    for i in range(N):
        temp = list(map(int, input().split()))
        A.append(temp[0])
        B.append(temp[1])

    P = int(input())
    C = []

    for i in range(P):
        C.append(int(input()))

    stop = [0]*5001

    for i in range(N):
        for j in range(A[i], B[i] + 1):
            stop[j] += 1

    print(f'#{x}', end=' ')
    for i in range(P):
        print(f'{stop[C[i]]}', end=' ')
    print()
