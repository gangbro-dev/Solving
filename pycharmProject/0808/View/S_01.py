import sys
sys.stdin = open('input.txt')

for x in range(10):
    T = int(input())
    count = 0
    # 각 인덱스에 빌딩의 높이 리스트
    Building_Tall = list(map(int, input().split()))
    # 좌 우 2칸의 최대 높이를 담을 변수
    side_Tall = 0
    # 문제 조건: 맨 앞 맨 뒤 2칸씩 건물이 존재하지 않는다 -> 건물이 존재하는 인덱스에 대해서 반복
    for i in range(2, T-2):
        # 좌 우 2칸의 최대 높이를 측정한다.
        side_Tall = max(Building_Tall[i+1], Building_Tall[i-1], Building_Tall[i+2], Building_Tall[i-2])
        # 조망권이 확보된 현재 빌딩의 층 수 = (현재 인덱스 빌딩 높이) - (좌우 2칸에 최대 높이)
        can_View = Building_Tall[i] - side_Tall
        # 조망권이 확보된 현재 빌딩의 층 수가 양수라면(존재한다면)
        if can_View > 0:
            count += can_View

    print(f'#{x+1} {count}')
