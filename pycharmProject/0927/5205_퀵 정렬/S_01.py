import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    print(f'#{Tc} {L[N//2]}')
