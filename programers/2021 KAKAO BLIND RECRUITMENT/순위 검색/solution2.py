from bisect import bisect_left

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

    for i in range(4):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    x4list[i][j][k][l].sort()

    answer = []
    for check_list in query:
        A, B, C, D = check_list.split(' and ')
        D, point = D.split()
        point = int(point)
        i, j, k, l = info_category[A], info_category[B], info_category[C], info_category[D]
        cnt = len(x4list[i][j][k][l]) - bisect_left(x4list[i][j][k][l], point)
        answer.append(cnt)

    return answer

# 테스트 1 〉	통과 (414.71ms, 39.6MB)
# 테스트 2 〉	통과 (412.89ms, 39.5MB)
# 테스트 3 〉	통과 (401.01ms, 39.1MB)
# 테스트 4 〉	통과 (371.97ms, 39.4MB)