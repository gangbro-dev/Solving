T = int(input())

for Tc in range(1, T+1):
    num_set = input()
    cnt_num = [0] * 10
    for num in num_set:
        cnt_num[int(num)] += 1

    babyjin_flag = 0

    for start in range(8):                                              # straight 확인
        if cnt_num[start] and cnt_num[start + 1] and cnt_num[start + 2]:
            cnt_num[start] -= 1
            cnt_num[start + 1] -= 1
            cnt_num[start + 2] -= 1
            babyjin_flag += 1
            if cnt_num[start] and cnt_num[start + 1] and cnt_num[start + 2]:
                cnt_num[start] -= 1
                cnt_num[start + 1] -= 1
                cnt_num[start + 2] -= 1
                babyjin_flag += 1

    for num in range(10):                                               # triplet 확인
        if cnt_num[num] >= 3:
            cnt_num[num] -= 3
            babyjin_flag += 1
            if cnt_num[num] >= 3:
                cnt_num[num] -= 3
                babyjin_flag += 1

    if babyjin_flag == 2:
        babyjin_flag = True
    else:
        babyjin_flag = False

    print(f'#{Tc} {babyjin_flag}')
