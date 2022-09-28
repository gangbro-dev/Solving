def solution(info, query):
    x4list = [[[[[], [], []] for ___ in range(3)] for __ in range(3)] for _ in range(4)]
    info_category = {'cpp': 1, 'java': 2, 'python': 3,
                     'backend': 1, 'frontend': 2,
                     'junior': 1, 'senior': 2,
                     'chicken': 1, 'pizza': 2,
                     '-': 0}
    for person in info:
        lang, FB, career, food, point = person.split()
        point = int(point)
        i, j, k, l = info_category[lang], info_category[FB], info_category[career], info_category[food]
        for ii in [0, i]:
            for jj in [0, j]:
                for kk in [0, k]:
                    for ll in [0, l]:
                        x4list[ii][jj][kk][ll].append(point)

    answer = []
    for check_list in query:
        A, B, C, D = check_list.split(' and ')
        D, point = D.split()
        point = int(point)
        i, j, k, l = info_category[A], info_category[B], info_category[C], info_category[D]
        cnt = 0
        for p in x4list[i][j][k][l]:
            if p >= point:
                cnt += 1
        answer.append(cnt)


    return answer
