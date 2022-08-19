import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    N = int(input())                                        # 학생 수
    runaway = []                                            # 도망치는 경로 저장
    for _ in range(N):
        start, end = tuple(map(int, input().split()))
        s = (start - 1) // 2                                # 출발점의 복도 번호
        e = (end - 1) // 2                                  # 도착점의 복도 번호
        runaway.append((s, e))                              # 도망치는 경로의 출발점과 도착점을 튜플로 저장
    corridor = [0]*200                                      # 방 앞의 복도에 지나가는 구간 설정
    for s, e in runaway:
        if s != e:
            for i in range(s, e+1):                         # 출발방 번호가 도착방 번호보다 크면
                corridor[i] += 1                            # 출발점부터 도착점까지 복도마다 카운트
            for i in range(s, e-1, -1):                     # 출발방 번호가 도착방 번호보다 작으면
                corridor[i] += 1                            # 출발점부터 도착점까지 복도마다 카운트
        else:
            corridor[s] += 1

    print(f'#{Tc} {max(corridor)}')




