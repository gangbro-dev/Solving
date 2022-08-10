import sys
sys.stdin = open('input.txt')

T = int(input())

for Tc in range(1, T+1):
    num_set = list(map(int, input().split()))
    N = len(num_set)
    cnt = 0
    for i in range(1, 0b1 << N): # 비트 연산을 이용해서 모든 부분집합의 경우의 수 체크. 공집합 제외를 위해서 1부터 출발
        sum_of_set = 0
        for j in range(N):
            if i & (0b1 << j):
                sum_of_set += num_set[j] # 비트연산을 이용해서 원하는 원소만 추출
        if sum_of_set == 0:
            cnt += 1
    # 한번이라도 합이 0이라면 참, 아니라면 거짓
    if cnt:
        print(f'#{Tc} 1')
    else:
        print(f'#{Tc} 0')


