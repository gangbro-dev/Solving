import sys
sys.stdin = open('input.txt')

T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    my_list = list(map(int, input().split()))

    for i in range(N):
        for j in range(N-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

    print(f'#{Tc} ', end='')
    print(*my_list)
