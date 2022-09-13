N, D = map(int, input().split())
from itertools import combinations as combi
short_cut = list()
for _ in range(N):
    a = tuple(map(int, input().split()))
    if a[1] <= D and a[1] - a[0] > a[2]:        # 유효한 지름길만 사용
        short_cut.append(a)

short_cut_len = []                              # 유효한 지름길 조합의 단축 길이 리스트
for i in short_cut:
    short_cut_len.append(i[1]-i[0]-i[2])        # 단축 길이 = 도착점 - 출발점 - 지름길 길이

for i in range(2, N+1):                         # 원소가 2개 이상인 조합에 대해서
    for j in combi(short_cut, i):
        flag = False                            # 원소끼리 겹치는 조합인가?
        for k in range(len(j)):
            for l in range(k+1, len(j)):
                if j[k][0] <= j[l][0] < j[k][1] or j[k][0] < j[l][1] <= j[k][1]:
                    flag = True
                    break
            if flag:
                break
        else:                                   # 겹치지 않는다면, 조합 내부의 총 줄어드는 길이를 저장
            temp = 0
            for x in j:
                temp += x[1]-x[0]-x[2]
            short_cut_len.append(temp)

best = max(short_cut_len)
print(D - best)
