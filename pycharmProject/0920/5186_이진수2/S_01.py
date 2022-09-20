import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    num = float(input())
    ans = ''
    for _ in range(13):
        num *= 2
        if num >= 1:
            num -= 1
            ans += '1'
        else:
            ans += '0'

        if num == 0:
            break
    else:
        ans = 'overflow'

    print(f'#{Tc} {ans}')
