import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for x in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    min_sum = sum(num_list)
    max_sum = min(num_list)

    for i in range(N - M + 1): # 총 구간의 개수는 (전체길이) - (구간 길이) + 1 이다.
        num_now = num_list[i: i + M] # 계산할 구간을 슬라이싱 한다.
        sum_now = 0
        for j in num_now: # 슬라이싱한 구간의 구간합을 구한다.
            sum_now += j
        if sum_now < min_sum:
            min_sum = sum_now
        if sum_now > max_sum:
            max_sum = sum_now

    print(f'#{x} {max_sum - min_sum}')
