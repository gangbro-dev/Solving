def solution(today, terms, privacies):
    term_dict = dict()
    for t in terms:
        a, b = t.split()
        term_dict[a] = int(b)
    answer = []
    # 날짜계산
    for p_idx in range(len(privacies)):
        sign_date, case = privacies[p_idx].split()
        sign_y, sign_m, sign_d = map(int, sign_date.split('.'))
        expire_m = sign_m + term_dict[case]
        # 만료년도 만들기
        expire_y = sign_y
        while expire_m > 12:
            expire_m = expire_m - 12
            expire_y += 1
        # 만료확인
        today_y, today_m, today_d = map(int, today.split('.'))
        if today_y == expire_y:
            if today_m == expire_m:
                if today_d >= sign_d:
                    answer.append(p_idx +1)
            elif today_m > expire_m:
                answer.append(p_idx + 1)
        elif today_y > expire_y:
            answer.append(p_idx + 1)

    return answer