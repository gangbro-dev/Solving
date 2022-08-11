import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    T = int(input())    # 인풋 파일에 테스트 번호가 각 케이스의 첫 줄에 주어지므로 여기서 받는다
    mat = []            # 사다리를 넣을 리스트
    for i in range(100):    # 사다리 받기
        mat.append(list(map(int, input().split())))

    for i in range(100):    # 출발점(사실 도착점) 찾기
        if mat[-1][i] == 2:
            r_now = i
    h_now = 99 # 출발점(사실 도착점) 높이
    lr = (-1, 1)
    while h_now > 0:    # 도착점(사실 출발점)에 도착할 때 까지 반복
        for i in lr:    # 좌, 우를 확인
            if 0 <= r_now+i < 100:  # 좌, 우의 인덱스가 리스트 이내인지 확인
                if mat[h_now][r_now+i]: # 좌, 우에 가로줄이 있다면,
                    while 0 <= r_now+i < 100 and mat[h_now][r_now+i]:  # 가로줄이 끝나거나, 인덱스 이내일때까지 전진 (단축 평가)
                        r_now = r_now+i
                    h_now -= 1  # 가로줄이 끝나면 무조건 한칸 올라가지
                    break
        else:    # 가로줄이 없다면, 위로 한칸 올라가기
            h_now -= 1

    print(f'#{T} {r_now}')  # 도착점 출력
