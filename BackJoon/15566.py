import sys
input = sys.stdin.readline

def frogSetting(N, frog, favleaf, frogNum=1):
    global state
    # 모든 개구리 배치 시 재귀 종료
    if frogNum > N:
        state[0] = True
        return True
    # 일단 한 마리 좋아하는 이파리 위에 올려봐
    for leaf in favleaf[frogNum]:
        # 이미 이파리위에 개구리가 있으면 다음 이파리 보기
        if state[leaf]:
            continue
        state[leaf] = frogNum
        # 주변 개구리 보자 -> 하나라도 불일치면 다음 확인
        for otherfrog, content in adjLog[leaf]:
            # 주변개구리 존재하면 확인 -> 존재하지 않으면 재귀 가능
            if state[otherfrog]:
                # 흥미도가 안맞다 -> 재귀불가
                if frog[state[otherfrog]][content] != frog[frogNum][content]:
                    # 초기화
                    state[leaf] = None
                    break
        # 모든 현재 이파리 주변에 적합하지 않은 개구리가 없다면 재귀하자
        else:
            if frogSetting(N, frog, favleaf, frogNum+1):
                return True
            # 이전 케이스가 실패했으면, 초기화
            state[leaf] = None

N, M = map(int, input().split())
frog = list((None,))
favleaf = [None] * (N+1)
adjLog = [[] for _ in range(N+1)]
for i in range(N):
    frog.append(tuple(map(int, input().split())))

for i in range(1, N+1):
    A, B = map(int, input().split())
    if A == B:
        favleaf[i] = (A,)
    else:
        favleaf[i] = (A, B)


for i in range(M):
    A, B, T = map(int, input().split())
    adjLog[A].append((B, T-1))
    adjLog[B].append((A, T-1))

state = [None] * (N + 1)
frogSetting(N, frog, favleaf)
if state[0]:
    print('YES')
    print(*state[1:])
else:
    print('NO')
