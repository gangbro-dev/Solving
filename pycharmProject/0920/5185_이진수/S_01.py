import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    N, my_hex = input().split()
    N = int(N)

    ans = ''
    for char in my_hex:
        ans += format(int(char, 16), '04b')

    print(f'#{Tc} {ans}')
