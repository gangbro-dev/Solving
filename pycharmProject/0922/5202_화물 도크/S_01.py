import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    time = []
    for _ in range(N):
        time.append(tuple(map(int, input().split())))
    time.sort(key=lambda x:x[1])

    ans = 0
    for i in range(N):
        set_end = time[i][1]
        set_len = 1
        for idx in range(i+1, N):
            if time[idx][0] >= set_end:
                set_len += 1
                set_end = time[idx][1]
        ans = max(ans, set_len)

    print(f'#{Tc} {ans}')
