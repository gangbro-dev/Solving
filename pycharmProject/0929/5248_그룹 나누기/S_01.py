def find(x, sets):
    a = x
    while sets[a] != a:
        a = sets[a]
    return a


def union(x, y, sets):
    if sets[x] == sets[y]:
        pass
    elif sets[x] < sets[y]:
        link(x, y, sets)
    else:
        link(y, x, sets)


def link(x, y, sets):
    a = find(y, sets)
    for _ in range(sets.count(a)):
        sets[sets.index(a)] = find(x, sets)


T = int(input())

for Tc in range(1, T+1):
    N, M = map(int, input().split())
    hope = list(map(int, input().split()))
    lst = [x for x in range(N + 1)]

    for i in range(M):
        union(hope[2 * i], hope[2 * i + 1], lst)
    ans = set(lst)

    print(f'#{Tc} {len(ans) - 1}')
