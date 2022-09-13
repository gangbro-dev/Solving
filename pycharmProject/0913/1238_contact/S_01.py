# import sys
# sys.stdin = open('sample_input.txt')
from collections import deque

for Tc in range(1, 11):
    N, start = map(int, input().split())        # 간선의 개수와 시작점
    # 노드는 총 1~100개. 인덱스로 접근하기 위해서 101개의 원소 세팅. 입력에 중복이 가능하므로 set으로 저장
    contact_list = [set() for _ in range(101)]
    line = list(map(int, input().split()))
    for i in range(len(line)//2):               # 모든 간선 정보를 저장
        a, b = line[i*2: i*2 + 2]
        contact_list[a].add(b)

    visit = [0] * 101                           # 몇 번째로 연락하는 곳인지 체크할 리스트. 노드마다 체크하크로 101개 세팅
    cnt = 1
    visit[start] = cnt                          # 출발점은 1로 저장
    last_visit = list()                         # 마지막 차례로 연락하는 곳들을 저장할 리스트
    next = deque([start])                       # queue를 이용해서 순차적으로 접근
    while next:
        node = next.popleft()                   # 전화를 시작할 노드를 팝
        for i in contact_list[node]:            # 연결된 간선에 대해서
            if not visit[i]:                    # 아직 연락을 받지 않았다면
                visit[i] = visit[node] + 1      # 연락 체크하고, 연락한 곳에서 +1차례를 가짐
                next.append(i)                  # 다음 연락 출발점으로 저장
                if cnt == visit[i]:             # 만약에 차례가 마지막이라면
                    last_visit.append(i)        # 마지막 차례로 저장
                elif cnt < visit[i]:            # 만약 새로운 마지막 차례라면
                    last_visit = [i]            # 새로 리스트를 초기화하고 값을 저장장
                    cnt += 1                    # 차례값을 1 올림

    print(f'#{Tc} {ma(last_visit)}')
