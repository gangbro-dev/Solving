import sys
sys.stdin = open('input.txt')

T = int(input())

for Tc in range(1, T+1):
    N, P = map(int, input().split())
    val = [N//P] * P
    rest = N % P
    for i in range(rest):
        val[i] += 1
    ans = 1
    for a in val:
        ans *= a
    print(f'#{Tc} {ans}')
