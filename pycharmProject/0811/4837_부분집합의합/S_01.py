import sys
sys.stdin = open('input.txt')

T = int(input())

for Tc in range(1, T+1):
    A = [x for x in range(1, 13)]
    N, K = map(int, input().split())
    ans = 0
    # 부분집합 경우의 수 추출
    for i in range(0b1 << 12):
        cnt = 0
        sum_of_set = 0
        for j in range(12):
            # 부분집합의 원소들을 합으로 바로 더함.
            # 원소의 수를 체크하기 위해서 cnt 사용
            if i & (0b1 << j):
                sum_of_set += A[j]
                cnt += 1
        # 부분집합의 크기와 그 합이 조건에 맞다면,
        if cnt == N and sum_of_set == K:
            ans += 1

    print(f'#{Tc} {ans}')
