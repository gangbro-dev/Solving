from itertools import combinations


def solution(orders, course):
    sorted_order = []
    for order in orders:
        sorted_order.append(sorted(order))

    course_menus = [[] for _ in range(max(course) + 1)]
    course_max_count = [1] * (max(course) + 1)
    for this_order_idx in range(len(sorted_order)):
        for course_len in course:
            if len(sorted_order[this_order_idx]) < course_len:  # 만약 메뉴의 길이가 코스의 길이보다 짧다면, 이후 모든 코스보다 짧으므로
                break
            for sub_comb in combinations(sorted_order[this_order_idx], course_len):
                sub_comb_max_count = 0
                for other_order in sorted_order[this_order_idx+1:]:     # 각 주문마다 이 셋이 존재하는지 확인
                    for menu in sub_comb:
                        if menu not in other_order:
                            break
                    else:                                               # 주문에 셋이 존재하면 카운트
                        sub_comb_max_count += 1
                if sub_comb_max_count > course_max_count[course_len]:               # 더 많은 주문 수를 가진 조합을 만난 경우
                    course_max_count[course_len] = sub_comb_max_count
                    course_menus[course_len] = [sub_comb]               # 저장 초기화 후 그 값 저장
                elif sub_comb_max_count == course_max_count[course_len]:            # 같은 주문 수를 가진 조합을 만난 경우
                    course_menus[course_len].append(sub_comb)           # 후보 코스 메뉴에 저장

    answer = []
    for best_courses in course_menus:
        for best_course in best_courses:
            answer.append(''.join(best_course))

    return sorted(answer)
