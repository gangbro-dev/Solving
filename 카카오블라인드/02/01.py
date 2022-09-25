def solution(cap, n, deliveries, pickups):

    while deliveries:
        if deliveries[-1]:
            break
        else:
            deliveries.pop()
    while pickups:
        if pickups[-1]:
            break
        else:
            pickups.pop()
    answer = 0
    while deliveries or pickups:
        answer += max(len(deliveries), len(pickups)) * 2
        # 출발할 때 싣는 짐 개수
        del_num = cap
        # 출발
        while deliveries and del_num:
            deli_now = deliveries.pop()
            del_num -= deli_now
            if del_num < 0:
                deliveries.append(-del_num)
                del_num = 0
        # deliveries 정리
        while deliveries:
            if deliveries[-1]:
                break
            else:
                deliveries.pop()
        pick_num = cap
        # 수거
        while pickups and pick_num:
            pick_now = pickups.pop()
            pick_num -= pick_now
            if pick_num < 0:
                pickups.append(-pick_num)
                pick_num = 0
        # pickups 정리
        while pickups:
            if pickups[-1]:
                break
            else:
                pickups.pop()

    return answer


cap = 4
n = 5
d = [1,0,3,1,2]
p = [0,3,0,4,0]
print(solution(cap, n, d, p))