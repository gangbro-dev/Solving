T = int(input())

for Tc in range(T):
    target = input()
    check_len = len(target) // 2
    d_start = 0
    d_end = 0
    palin_flag = 0
    i = 0
    while i < check_len:
        start = i + d_start
        end = -(i + 1) - d_end
        if target[start] == target[end]:
            i += 1
        else:
            # 양쪽 다 건너뛰기가 가능한 경우
            if palin_flag == 0 and target[start + 1] == target[end] and target[start] == target[end - 1]:
                palin_flag = 1
                palin_left = 1
                palin_right = 1
                d_start = 1
                d_end = 1
                temp = i
                while i < check_len:  # 왼쪽 건너뛰기 하면 회문인지 체크
                    start = i + d_start
                    end = -(i + 1)
                    if target[start] == target[end]:
                        i += 1
                    else:  # 회문이 아니라면
                        palin_left = 2
                        break
                i = temp
                while i < check_len:  # 오른쪽 건너뛰기 하면 회문인지 체크
                    start = i
                    end = -(i + 1) - d_end
                    if target[start] == target[end]:
                        i += 1
                    else:
                        palin_right = 2
                        break
                palin_flag = min(palin_left, palin_right)  # 두 경우 중 하나라도 회문이라면 유사 회문
                break
            # 왼쪽 하나 건너뛰면 성립하는 경우
            elif palin_flag == 0 and target[start + 1] == target[end]:
                d_start = 1
                palin_flag = 1
                i += 1
            # 오른쪽 하나 건너뛰면 성립하는 경우
            elif palin_flag == 0 and target[start] == target[end - 1]:
                d_end = 1
                palin_flag = 1
                i += 1
            else:
                palin_flag = 2
                break

    print(palin_flag)
