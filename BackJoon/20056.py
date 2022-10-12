N, M, K = map(int, input().split())
delta = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
FireBall = list()

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    r, c = r-1, c-1
    FireBall.append([r, c, m, s, d])

for command in range(K):
    loc_set = set()
    mat = [[[] for _ in range(N)] for __ in range(N)]
    cnt = 0
    for idx in range(len(FireBall)):
        r, c, m, s, d = FireBall[idx]
        dr, dc = delta[d]
        nr, nc = (r + (dr * s)) % N, (c + (dc * s)) % N
        mat[nr][nc].append(idx)
        FireBall[idx] = [nr, nc, m, s, d]
        loc_set.add((nr, nc))
    newFireBall = list()
    for loc in loc_set:
        x, y = loc
        if len(mat[x][y]) == 1:
            newFireBall.append(FireBall[mat[x][y][0]])
        else:
            m_sum = 0
            s_sum = 0
            flag1, flag2 = False, False
            for idx in mat[x][y]:
                m_sum += FireBall[idx][2]
                s_sum += FireBall[idx][4]
                if not (flag1 and flag2):
                    if FireBall[idx][3] % 2:
                        flag1 = True
                    else:
                        flag2 = True
            nm = m_sum//5
            if nm == 0:
                continue
            ns = s_sum//len(mat[x][y])
            if flag1 and flag2:
                newFireBall.append([x, y, nm, ns, 1])
                newFireBall.append([x, y, nm, ns, 3])
                newFireBall.append([x, y, nm, ns, 5])
                newFireBall.append([x, y, nm, ns, 7])
            else:
                newFireBall.append([x, y, nm, ns, 2])
                newFireBall.append([x, y, nm, ns, 4])
                newFireBall.append([x, y, nm, ns, 6])
                newFireBall.append([x, y, nm, ns, 8])
    FireBall = newFireBall

ans = 0
for ball in FireBall:
    ans += ball[2]
print(ans)