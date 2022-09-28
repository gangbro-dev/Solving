from itertools import combinations


def solution(orders, course):
    ASCII_factor = ord('A')
    alpha_count = [0] * 27
    max_order_len = 0
    # 2번 이상 주문된 메뉴만 골라서 조합으로 구성할 것임
    for order in orders:
        for menu in order:
            alpha_count[ord(menu) - ASCII_factor] += 1
        max_order_len = max(len(order), max_order_len)
    alpha_set = set()
    for idx in range(len(alpha_count)):
        if alpha_count[idx] > 1:
            alpha_set.add(chr(idx + ASCII_factor))

    alpha_list = sorted(list(alpha_set))                        # 알파벳 오름차순
    course_menus = [[] for _ in range(max(course) + 1)]
    for course_len in course:                                   # 모든 세트메뉴의 길이에 대해서
        if max_order_len < course_len:                          # 손님이 시킨 메뉴의 최대길이가 세트메뉴 길이보다 작으면
            continue                                            # 그 길이만큼 시킨 주문이 존재할 수 없음
        course_max_count = 2                                    # 최소 2명에게 주문받은 세트이므로
        for sub_comb in combinations(alpha_list, course_len):   # 세트메뉴의 길이로 이루어진 집합 생성 -> 오름차순으로 생성
            sub_comb_max_count = 0
            for order in orders:                                # 각 주문마다 이 셋이 존재하는지 확인
                                                                # 존재하면 카운트할 변수
                for menu in sub_comb:
                    if menu not in order:
                        break
                else:                                           # 주문에 셋이 존재하면 카운트
                    sub_comb_max_count += 1
            if sub_comb_max_count > course_max_count:
                course_max_count = sub_comb_max_count
                course_menus[course_len] = [sub_comb]
            elif sub_comb_max_count == course_max_count:
                course_menus[course_len].append(sub_comb)
    answer = []
    for best_courses in course_menus:
        for best_course in best_courses:
            answer.append(''.join(best_course))

    return sorted(answer)


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

print(solution(orders, course))