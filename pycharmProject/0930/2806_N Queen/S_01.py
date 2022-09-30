import sys
sys.stdin = open('sample_input.txt')


# col = 세로줄 체크용 셋
# a = 좌상-우하 대각선 체크용 셋 x - y in (x, y)
# b = 우상-좌하 대각선 체크용 셋 x + y in (x, y)
def n_queen(n, col=set(), a=set(), b=set(), row=0):
    if row == n:
        return 1
    cnt = 0
    for i in range(n):
        if i in col or row-i in a or row+i in b:
            continue
        else:
            new_col = col | {i}
            new_a = a | {row-i}
            new_b = b | {row+i}
            cnt += n_queen(n, new_col, new_a, new_b, row+1)
    return cnt


T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    ans = n_queen(N)
    print(f'#{Tc} {ans}')
