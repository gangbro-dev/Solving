import sys
sys.stdin = open('input.txt')

T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    my_list = list(map(int, input().split()))
    i = 0
    result_list = []
    while i < 5:    # (최댓값1번, 최솟값1번)X 5 = 10개!
        # 최댓값을 맨 오른쪽으로!
        for j in range(len(my_list)-1):     # 리스트 길이가 변하므로, 가변되는 리스트 길이를 반영
            if my_list[j] > my_list[j+1]:   # 왼쪽 원소가 오른쪽 원소보다 크다면
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]     #자리 바꾸기
        result_list.append(my_list.pop())   # 맨 오른쪽 원소를 뽑아서 결과 리스트에 저장
        # 최솟값을 맨 오른쪽으로!
        for j in range(len(my_list) - 1):  # 리스트 길이가 변하므로, 가변되는 리스트 길이를 반영
            if my_list[j] < my_list[j + 1]:  # 왼쪽 원소가 오른쪽 원소보다 작다면
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]  # 자리 바꾸기
        result_list.append(my_list.pop())   # 맨 오른쪽 원소를 뽑아서 결과 리스트에 저장
        i += 1

    print(f'#{Tc}', end=' ')
    print(*result_list)
