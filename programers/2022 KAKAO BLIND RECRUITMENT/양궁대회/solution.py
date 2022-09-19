def solution(
        n,
        info
):
    score_nums = list(map(lambda x: x + 1, info))
    value_per_shot = []
    for i in range(11):
        if info[i]:
            value = 2 * (10 - i) / score_nums[i]
            value_per_shot.append(value)
        else:
            value_per_shot.append(10 - i)

    # 라이언이 쏘는 화살 계산
    # 우선 가장 화살 당 가치가 높은 점수부터 노린다. -> 최고득점을 알기 위해서
    # 화살 당 가치가 같은 점이 있다면, 가장 낮은 점수 구역부터 노린다.
    # 어떤 곳도 남은 화살로 득점할 수 없다면, 남은 화살은 0점으로 보낸다
    lion = [0] * 11
    arrow = n
    while arrow:
        max_value = 0
        idx = 100  # 에러가 나는 숫자

        for i in range(len(value_per_shot)):
            if value_per_shot[i] and arrow >= score_nums[i] and max_value <= value_per_shot[i]:
                max_value = value_per_shot[i]
                idx = i
        # 남은 화살로 득점할 수 있는 어떠한 점이 존재할 때, 남은 화살에서 필요한 화살을 빼서 그 구역에 투자
        # 그 구역은 더 이상 화살을 투자해도 득점할 수 없으므로, 가치를 0으로 조정
        if idx < 20:
            lion[idx] = score_nums[idx]
            arrow -= score_nums[idx]
            value_per_shot[idx] = 0
        # 남은 화살이 더 이상 어느곳에서도 득점할 수 없다면, 가장 낮은 칸인 0에 버림
        else:
            lion[10] = arrow
            arrow = 0
            # 최고점을 노릴 수 있는 경우를 시행했는데도 점수가 넘지 못하면 [-1], 아니면 배열 작성
    score = 0
    for i in range(11):
        if lion[i] > info[i]:
            score += 10 - i
        elif not info[i]:
            pass
        else:
            score -= 10 - i

    if score > 0:
        answer = lion
    else:
        answer = [-1]
    return answer

n = 2
info = [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]

print(solution(n, info))