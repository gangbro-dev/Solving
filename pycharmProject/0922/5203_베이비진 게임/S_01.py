import sys
sys.stdin = open('sample_input.txt')


def is_baby_gin(cnt_num):
    babyjin_flag = 0

    for start in range(8):  # straight 확인
        if cnt_num[start] and cnt_num[start + 1] and cnt_num[start + 2]:
            cnt_num[start] -= 1
            cnt_num[start + 1] -= 1
            cnt_num[start + 2] -= 1
            babyjin_flag += 1

    for num in range(10):  # triplet 확인
        if cnt_num[num] >= 3:
            cnt_num[num] -= 3
            babyjin_flag += 1

    if babyjin_flag:
        babyjin_flag = True
    else:
        babyjin_flag = False

    return babyjin_flag


T = int(input())

for Tc in range(1, T+1):
    num_set = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    ans = 0
    for i in range(6):
        player1[num_set[2 * i]] += 1
        player2[num_set[2 * i + 1]] += 1
        if is_baby_gin(player1):
            ans = 1
            break
        if is_baby_gin(player2):
            ans = 2
            break

    print(f'#{Tc} {ans}')
