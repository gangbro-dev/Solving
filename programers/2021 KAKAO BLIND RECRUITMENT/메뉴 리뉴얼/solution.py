def solution(orders, course):
    order_dict = dict()
    for i in range(len(orders)):
        for menu in orders[i]:
            if menu not in order_dict.keys():
                order_dict[menu] = [i]
            else:
                order_dict[menu].append(i)

    menu
    return answer