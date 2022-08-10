import sys
sys.stdin = open('input.txt')

T = int(input())

for x in range(T):
    N = int(input())
    Box_list = list(map(int, input().split()))
    Max_drop = 0
    for i in range(N):
        count = 0
        for j in range(i+1, N):
            if Box_list[i] > Box_list[j]:
                count += 1
        if Max_drop < count:
            Max_drop = count
    print(f'#{x+1} {Max_drop}')
