# 부분집합을 이용한 풀이 -> 반례찾기 실패
# N, D = map(int, input().split())
# from itertools import combinations as combi
# short_cut = list()
# for _ in range(N):
#     a = tuple(map(int, input().split()))
#     if a[1] <= D and a[1] - a[0] > a[2]:        # 유효한 지름길만 사용
#         short_cut.append(a)
#
# short_cut_len = []                              # 유효한 지름길 조합의 단축 길이 리스트
# for i in short_cut:
#     short_cut_len.append(i[1]-i[0]-i[2])        # 단축 길이 = 도착점 - 출발점 - 지름길 길이
#
# for i in range(2, N+1):                         # 원소가 2개 이상인 조합에 대해서
#     for j in combi(short_cut, i):
#         flag = False                            # 유효한 조합인지 확인(출발점, 도착점을 확인해서 겹치는 구간인지 확인)
#         for k in range(len(j)):
#             for l in range(k+1, len(j)):
#                 if j[k][0] <= j[l][0] < j[k][1] or j[k][0] < j[l][1] <= j[k][1]:
#                     flag = True
#                     break
#             if flag:
#                 break
#         else:                                   # 겹치지 않는다면, 조합 내부의 총 줄어드는 길이를 저장
#             temp = 0
#             for x in j:
#                 temp += x[1]-x[0]-x[2]
#             short_cut_len.append(temp)
#
# best = max(short_cut_len)
# print(D - best)

# 2. 다익스트라 도전!
N, D = map(int, input().split())
# 기본적인 거리로 테이블 초기화
cost_table = [x for x in range(D + 1)]          # 지름길 없이 도로 타면 기본 테이블
# 지름길 입력
short_cut_list = list()
for _ in range(N):
    a = tuple(map(int, input().split()))
    if a[1] <= D and a[1] - a[0] > a[2]:        # 유효한 지름길만 사용
        short_cut_list.append(a)
# 지름길 도착점이 가장 앞쪽인 순으로 정렬
short_cut_list.sort(key=lambda x: x[1])

for short_cut in short_cut_list:
    # 지름길 도착점까지의 비용이 새로운 최소비용이라면 갱신
    if cost_table[short_cut[1]] > cost_table[short_cut[0]] + short_cut[2]:
        cost_table[short_cut[1]] = cost_table[short_cut[0]] + short_cut[2]
        # 갱신한 최소비용 값을 이용해서 모든 다음 지점들의 비용 갱신
        for x in range(short_cut[1], D):
            cost_table[x+1] = cost_table[x] + 1

print(cost_table[-1])


