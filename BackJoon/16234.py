N, L, R = map(int, input().split())

# 연합들을 구하는 함수
# 연합마다 연합에 속하는 땅 인덱스를 묶어놓은 셋을 반환한다.
def union(N_list, L, R):
    from collections import deque
    union_list = []
    union_count = -1
    visit = [[False for _ in range(N)] for _ in range(N)]
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    que = deque()
    for row in range(N):
        for column in range(N):
            if visit[row][column]:
                continue
            que.append((row, column))
            visit[row][column] = True
            while que:
                x, y = que.popleft()
                for dx, dy in delta:
                    if 0 <= x+dx < N and 0 <= y+dy < N:
                        if not visit[x + dx][y + dy]:
                            if L <= abs(N_list[x][y] - N_list[x+dx][y+dy]) <= R:
                                que.append((x + dx, y + dy))
                                visit[x + dx][y + dy] = True
                                a = (x, y)
                                b = (x+dx, y+dy)
                                for i in union_list:
                                    if a in i:
                                        i.append(b)
                                        break
                                    if b in i:
                                        i.append(a)
                                        break
                                else:
                                    union_list.append([])
                                    union_count += 1
                                    union_list[union_count].append(a)
                                    union_list[union_count].append(b)
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
