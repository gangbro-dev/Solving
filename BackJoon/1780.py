ans = [0, 0, 0] # 답을 넣을 리스트 -1 0 1


def papercheck(paper, papers, papere, N):
    global ans
    xs, ys = papers
    xe, ye = papere
    for i in range(xs, xe):
        for j in range(ys, ye):
            if paper[i][j] != paper[xs][ys]:
                N //= 3
                for ii in range(3):
                    for jj in range(3):
                        s = (papers[0] + (N * ii), papers[1] + (N * jj))
                        if N == 1:
                            ans[paper[s[0]][s[1]]] += 1
                        else:
                            e = (papers[0] + (N * (ii + 1)), papers[1] + (N * (jj + 1)))
                            papercheck(paper, s, e, N)
                return
    ans[paper[xs][ys]] += 1
    return


N = int(input())

paper = list()
ㅁㅇ
for i in range(N):
    paper.append(list(map(int, input().split())))

papercheck(paper, (0, 0), (N, N), N)

for i in range(-1, 2):
    print(ans[i])
