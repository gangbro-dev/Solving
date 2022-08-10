import sys
sys.stdin = open('input.txt')

T = int(input())

for x in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    num_min = 1000001
    num_max = 0
    for i in num:
        if num_min > i:
            num_min = i
        if num_max < i:
            num_max = i

    print(f'#{x} {num_max - num_min}')
