import sys
sys.stdin = open('input.txt')

T = int(input())

for x in range(T):
    N = int(input())
    # 각 줄의 박스 높이를 리스트로 받음
    Box_list = list(map(int, input().split()))
    # 최대 낙차를 저장할 Max_drop 선언
    Max_drop = 0
    for i in range(N):
        count = 0
        for j in range(i+1, N):
            if Box_list[i] > Box_list[j]:
                count += 1
        if Max_drop < count:
            Max_drop = count
    print(f'#{x+1} {Max_drop}')