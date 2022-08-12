import sys
sys.stdin = open('input.txt')

T = int(input())

for Tc in range(1, T+1):
    max_cnt = 0
    cnt = 0
    N = int(input())
    my_str = input()
    for i in my_str:
        if i == '1':
            cnt += 1
            max_cnt = max(cnt, max_cnt)
        elif i == '0':
            cnt = 0

    print(f'#{Tc} {max_cnt}')
