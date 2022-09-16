import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    # 이진탐색 시작, 끝점 확인.
    start, end = 1, 10
    # 탐색하는 수의 최댓값 10^18, 따라서 정답의 최댓값 10^6
    # 이를 이용해서 이진탐색의 범위를 축소해보자
    for i in range(1, 6):
        if end ** 3 > N:
            break
        else:
            start = end
            end *= 10
    # 이진탐색. 중간값(시작 + 끝 // 2)을 이용해서 좌측인지, 우측인지 확인한다.
    ans = -1            # 초기값은 답이 없을 때를 상정한다.
    while True:
        point = (start + end) // 2
        temp = point ** 3
        if temp == N:
            ans = point
            break
        elif temp < N:
            start = point + 1
        else:
            end = point - 1
        if start > end:
            break

    print(f'#{Tc} {ans}')
