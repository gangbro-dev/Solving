

N, L, R = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


# 연합들을 구하는 함수
# 연합마다 연합에 속하는 땅 인덱스를 묶어놓은 셋을 반환한다.
def union(N_list, L, R):
    from collections import deque
    que = deque()
    que.append((0, 0))
    union_list = []
    union_count = 0
    visit = [[False for _ in range(N)] for _ in range(N)]
    while True:
        row, column = que.popleft()
        visit[column][row] = True
        for i in range(4):
            # 비교할 칸이 인덱스 이내의 칸인지 확인
            if 0 <= row + dx[i] < N and 0 <= column + dy[i] < N:
                # 현재 인덱스와 한칸 오른쪽의 인덱스를 비교해서 연합인지 확인
                if L <= abs(N_list[column][row]-N_list[column+dy[i]][row+dx[i]]) <= R:
                    # 연합이고, 방문한 적이 없다면, 대기열에 추가
                    if not visit[column+dy[i]][row+dx[i]]:
                        que.append((column+dy[i], row+dx[i]))
                    # 연합국이라면, 현재 양 국이 속해있는 연합이 존재하는지 확인
                    # 존재한다면, 그 쪽 연합으로 나머지 국가 합류
                    for j in range(union_count):
                        if (column, row) in union_list[j]:
                            union_list[j].add((column+dy[i], row+dx[i]))
                            break
                        elif (column+dy[i], row+dx[i]) in union_list[j]:
                            union_list[j].add((column, row))
                            break
                    # 만약 현재 존재하는 연합에 존재하는 원소가 아닌 경우, 새연합 셋을 생성 후 둘 다 대입
                    else:
                        union_list.append(set())
                        union_list[union_count].add((column, row))
                        union_list[union_count].add((column+dy[i], row+dx[i]))
                        union_count += 1
        for i in range(N):
            for j in range(N):
                if visit[i][j]:
                    pass
                else:
                    que.append((i, j))
                    break
            if que:
                break
        else:
            break

    # 연합이 존재하지 않는다면,
    if not union_list:
        return False
    # 각 연합마다 연합원의 인덱스를 가진 리스트 반환
    return union_list

# 인구 움직이기 함수
# 위 함수에서 구한 연합셋을 가지고, 연합마다 인구이동을 실행한다.
# 인구이동을 한다면 1을, 안한다면 0을 반환한다.

def pop_move(N_list, union_list):
    # 연합이 존재한다면,
    if union_list:
        for union in union_list:
            # 각 연합 셋의 원소합 구하기
            pop_sum = 0
            for idx in union:
                x, y = idx
                pop_sum += N_list[x][y]
            # 인구 이동 시 인구수. 나머지는 버리므로, 몫으로 계산
            pop_avg = pop_sum//len(union)
            # 인구 이동
            for idx in union:
                x, y = idx
                N_list[x][y] = pop_avg
        return 1
    else:
        return 0

# 메인 함수


N_list = []

for _ in range(N):
    N_list.append(list(map(int, input().split())))

check = True
cnt = 0

# check에 pop_move 함수의 반환값을 받는다. 0이면 인구이동이 일어나지 않으므로, 반복문 탈출
while check:
    check = pop_move(N_list, union(N_list, L, R))
    cnt += check

print(cnt)
