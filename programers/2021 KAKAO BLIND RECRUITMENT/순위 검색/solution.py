import bisect

def solution(info, query):
    people = []
    people_info = dict()
    info_category = ['cpp', 'java', 'python',
                     'backend', 'frontend',
                     'junior', 'senior',
                     'chicken', 'pizza']
    for i in info_category:
        people_info[i] = set()
    cnt = 0
    for person in info:
        lang, FB, career, food, point = person.split()
        people.append([lang, FB, career, food, int(point)])
        for x in [lang, FB, career, food]:
            people_info[x].add(cnt)
        cnt += 1

    answer = []
    DP = dict()
    for check_list in query:
        A, B, C, D = check_list.split(' and ')
        D, point = D.split()
        point = int(point)
        temp = range(len(people))
        if A+B+C+D in DP.keys():
            temp = DP[A+B+C+D]
            answer.append(len(temp) - bisect.bisect_left(temp, point))
        else:
            for check in [A, B, C, D]:
                if check != '-':
                    if type(temp) is set:
                        temp = temp & people_info[check]
                    else:
                        temp = people_info[check]

            points = []
            for i in temp:
                points.append(people[i][4])
            points.sort()
            DP[A+B+C+D] = points
            answer.append(len(points) - bisect.bisect_left(points, point))

    return answer

# 테스트 1 〉	통과 (537.19ms, 69.7MB)
# 테스트 2 〉	통과 (526.45ms, 70MB)
# 테스트 3 〉	통과 (545.01ms, 69.4MB)
# 테스트 4 〉	통과 (502.19ms, 70.2MB)