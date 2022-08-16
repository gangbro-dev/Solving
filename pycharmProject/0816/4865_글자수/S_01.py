import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    N = input()
    M = input()
    max_cnt = 0
    check_set = set()
    for i in N:
        if i in check_set:
            continue
        else:
            check_set.add(i)
        max_cnt = max(M.count(i), max_cnt)
    print(f'#{Tc} {max_cnt}')
