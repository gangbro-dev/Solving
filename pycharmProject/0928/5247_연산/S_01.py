import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    S, G = map(int, input().split())
    check = set([S])
    start = [S]
    cnt = 0
    while G not in check:
        temp = []
        for node in start:
            for next in [node + 1, node - 1, node * 2, node - 10]:
                if 0 < next <= 1000000 and next not in check:
                    temp.append(next)
                    check.add(next)
        cnt += 1
        start = temp[:]

    print(f'#{Tc} {cnt}')
