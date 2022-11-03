N, K = map(int, input().split())

dolls = tuple(map(int, input().split()))

idx = list()
for i in range(len(dolls)):
    if dolls[i] == 1:
        idx.append(i)

ans = -1
if len(idx) >= K:
    ans = len(dolls)
    for i in range(K - 1, len(idx)):
        if ans > idx[i] - idx[i - K + 1] + 1:
            ans = idx[i] - idx[i - K + 1] + 1
print(ans)
