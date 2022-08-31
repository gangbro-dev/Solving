# 우리가 원하는것 = 시간대가 몇개나 겹치는가
# 방법 1
# 시간 테이블을 만들어서 강의 시간이 존재하는 시간인 경우 +1을 하여 맥스값을 찾는다
# Fail. 시간테이블의 크기가 최대 10억이라서 메모리 에러가 남
#
# 방법 2
# 시간대 별로 딕셔너리를 만들어볼까?
# Fail. 역시나 이딴 편법으로 통과될 리가 없지
# N = int(input())
# classroom = [1] * (N+1)
# timetable = {}
# for Tc in range(N):
#     num, start, end = map(int, input().split())
#     for time in range(start, end):
#         if time in timetable.keys():
#             timetable[time] += 1
#         else:
#             timetable[time] = 1
#
# print(max(timetable.values()))
#
# 방법 3. 겹치는 시간대를 표현하는 튜플을 이용해서 모든 시간대를 조사해볼까?
# Fail -> 시간초과
# set으로 너무 많은 튜플생성을 방지 -> 시간초과
# set에서 큰 튜플 생성, 작은 튜플 제거로 연산속도 증가 해보자 -> 시간초과
# set 조작하는 것을 좀 정리해서 표현해보자 -> 시간초과
# 3번 폐기합시다
# N = int(input())
# timetable = []
#
# for Tc in range(N):
#     num, start, end = map(int, input().split())
#     timetable.append((start, end))
#
# classroom = {1: set()}
#
#
# for time1 in timetable:
#     classroom[1].add(time1)
#     for compare in sorted(classroom.keys(), reverse=True):
#         temp = classroom[compare].copy()
#         for time2 in temp:
#             # 같은 경우 비교 작업 제거
#             if time1 == time2:
#                 continue
#             # time2가 time1 을 포함하는 시간대인 경우
#             if time2[0] <= time1[0] < time2[1] and time2[0] <= time1[1] < time2[1] and time1[0] != time1[1]:
#                 if compare+1 in classroom.keys():
#                     classroom[compare+1].add((time1[0], time1[1]))
#                 else:
#                     classroom[compare+1] = {(time1[0], time1[1])}
#                 classroom[compare].add(time2)
#                 classroom[compare].discard(time1)
#             # time1가 time2 을 포함하는 시간대인 경우
#             elif time1[0] <= time2[0] < time1[1] and time1[0] <= time2[1] < time1[1] and time2[0] != time2[1]:
#                 if compare+1 in classroom.keys():
#                     classroom[compare+1].add((time2[0], time2[1]))
#                 else:
#                     classroom[compare+1] = {(time2[0], time2[1])}
#                 classroom[compare].discard(time2)
#             # time2의 시작점이 time1의 이내에 존재하는 경우
#             elif time1[0] <= time2[0] < time1[1]:
#                 if compare+1 in classroom.keys():
#                     classroom[compare+1].add((time2[0], time1[1]))
#                 else:
#                     classroom[compare+1] = {(time2[0], time1[1])}
#                 classroom[compare].add((time1[0], time2[1]))
#                 classroom[compare].discard(time2)
#                 classroom[compare].discard(time1)
#             # time2의 끝점이 time1의 이내에 존재하는 경우
#             elif time1[0] <= time2[1] < time1[1]:
#                 if compare+1 in classroom.keys():
#                     classroom[compare+1].add((time1[0], time2[1]))
#                 else:
#                     classroom[compare+1] = {(time1[0], time2[1])}
#                 classroom[compare].add((time2[0], time1[1]))
#                 classroom[compare].discard(time2)
#                 classroom[compare].discard(time1)
#             else:
#                 classroom[compare].add(time2)
#
# print(max(classroom.keys()))

# 방법 4 (질문게시판 확인함)
# 시작 시간을 정렬해서 하나의 큐
# 끝 시간을 정렬해서 하나의 큐
# 시작과 끝 큐로 아웃풋 값끼리 비교해서 작은 값을 팝하고 카운트 +-1
# 같다면, 종료시점이 우선되므로 카운트 -1 하고 그 다음 다시 카운트 +1
# 시작점 끝까지 계산 -> 끝 값이 남았어도 카운트값이 줄어들 순간 밖에 남지 않은 것이므로 상관 없음
# 최댓값이 된 경우를 출력 -> 틀림 시발? 왜지 -> 같을 때 우선순위가 바뀜

N = int(input())
start = list()
end = list()

for Tc in range(N):
    num, start_time, end_time = map(int, input().split())
    start.append(start_time)
    end.append(end_time)

start.sort()
end.sort()

start_idx = 0
end_idx = 0
cnt = 0
ans = 0
while start_idx < N:
    if start[start_idx] >= end[end_idx]:
        end_idx += 1
        cnt -= 1
    else:
        start_idx += 1
        cnt += 1
        ans = max(ans, cnt)

print(ans)
