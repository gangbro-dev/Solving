N, M = map(int, input().split())

tnum, *tpeople = map(int, input().split())

truth = set()
for i in tpeople:
    truth.add(i)
cnt = 0
party = []

for i in range(M):
    ppeople = list(map(int, input().split()))
    ppeople = set(ppeople[1:])
    party.append(ppeople)
flag = True

while flag:
    b_truth = set(truth)
    for i in party:
        if i & truth:
            truth |= i
    if truth == b_truth:
        flag = False


for i in party:
    if i & truth:
        pass
    else:
        cnt += 1

print(cnt)
