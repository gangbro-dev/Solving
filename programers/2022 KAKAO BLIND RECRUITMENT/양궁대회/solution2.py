from itertools import combinations_with_replacement as comb


def solution(n, info):
    answer = [-1]
    max_score = 0
    answer_set = list()
    # 0~10의 정수를 중복 조합으로 n개 뽑는다
    for point_set in comb(list(range(11)), n):          # [10, 10, 10]
        # 뽑은 조합을 통해서 lion이 맞춘 화살 리스트를 생성한다.
        lion = [0] * 11
        for point in point_set:
            lion[10-point] += 1                         # [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # lion 화살 리스트와 info를 비교해서 점수 차를 계산한다.
        score = 0
        for i in range(11):
            if lion[i] > info[i]:
                score += 10 - i
            elif info[i]:
                score -= 10 - i
        # 점수차를 최대 점수차와 비교해서 가장 큰 점수 차 조합을 생성한다.
        if score > max_score:
            max_score = score
            answer_set = list()
            answer_set.append(lion)
        elif score == max_score and max_score != 0:
            answer_set.append(lion)
        # 정답이 존재한다면
    if answer_set:
        answer = answer_set[0]
        # 정답이 2개 이상이라면
        if len(answer_set) > 1:
            # 가장 낮은 화살을 포함하는 정답 출력
            for ans in answer_set:
                for i in range(11):
                    if answer[10-i]:
                        if ans[10-i] > answer[10-i]:
                            answer = ans
                        break
    return answer

print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))