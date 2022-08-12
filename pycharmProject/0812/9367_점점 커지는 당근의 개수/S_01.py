import sys
sys.stdin = open('input.txt')

T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))
    cnt = 1
    max_cnt = cnt

    for i in range(N-1):
        if carrot[i] < carrot[i+1]:
            cnt += 1
            max_cnt = max(cnt, max_cnt)
        else:
            cnt = 1

    print(f'#{Tc} {max_cnt}')
