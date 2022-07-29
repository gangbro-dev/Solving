N, K = map(int, input().split())
cnt = 0
overN = 0
overcnt = 111111
while True:
    if K == N: # N 과 K가 같으면
        break
    if N == 0: # N 이 0이면
        N += 1
        cnt += 1
    if N < K: # N 이 K 보다 작으면
        N *= 2
        cnt += 1
    else:
        if not cnt: # 처음부터 N이 크면
            break
        elif (N-K) > K-(N/2): # N*2 와 N 중에 뭐가 K에 더 가까운가
            N //= 2
            cnt -= 1
        break
    # N이 범위를 초과하면 항
    if N > 100000: 
        overN = N
        overcnt = 0
        while overN >= 100000:
            overN -= 2**cnt
            overcnt += 1
        break

if N > 100000:
    N //= 2
    cnt -= 1

diff = abs(N - K)
double_times = cnt
if not diff:
    pass
else:
    for i in range(double_times):
        if diff%2:
            diff//=2
            cnt += 1
        else:
            diff//=2
if overcnt > diff:
    cnt += diff
else:
    diff = abs(overN - K)
    for i in range(double_times+1):
        if diff%2:
            diff//=2
            cnt += 1
        else:
            diff//=2
    cnt += overcnt + diff

print(cnt)
