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
        people_info[lang].add(cnt)
        people_info[FB].add(cnt)
        people_info[career].add(cnt)
        people_info[food].add(cnt)
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
        else:
            for check in [A, B, C, D]:
                if check != '-':
                    if type(temp) is set:
                        temp = temp & people_info[check]
                    else:
                        temp = people_info[check]
            DP[A+B+C+D] = temp
        points = []
        for i in temp:
            points.append(people[i][4])
        answer.append(len(points) - bisect.bisect_left(sorted(points), point))

    return answer
