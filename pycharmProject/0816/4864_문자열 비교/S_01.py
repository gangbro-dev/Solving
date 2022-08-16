# import sys
# sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    str1 = input()
    str2 = input()
    find_flag = 0
    jump_dict = dict()
    cnt = 1
    for i in str1[-2::-1]:
        if i in jump_dict.keys():
            pass
        else:
            jump_dict[i] = cnt
        cnt += 1
    i = 0
    # 보이어-무어 알고리즘. 범위를 초과했거나, 일치한 경우를 찾으면 탈출
    while not find_flag and i < len(str2) - len(str1) + 2:
        # 윈도우 만들기 만약, 윈도우가 작게 만들어진다면, 그건 윈도우가 마지막구간에 도달했다는 뜻이므로 마지막 구간을 체크
        window = str2[i:i+len(str1)]
        if len(window) != len(str1):
            window = str2[-len(str1):]
        jump = len(window)   # 몇 칸이나 넘어갈 지 정하는 변수

        # 뒤에서 부터 비교. 만약 모두 일치한다면, flag를 1로 한다.
        for j in range(1, len(str1)+1):
            if str1[-j] != window[-j]:
                break
        else:
            find_flag = 1

        # 몇 칸이나 넘어갈 지 평가
        # if not find_flag:
        #     if window[-1] in str1:
        #         if (str1.index(window[-1]) + 1) != len(window):
        #             jump = len(window) - (str1.index(window[-1]) + 1)
        if not find_flag:
            if window[-1] in jump_dict.keys():
                jump = jump_dict[window[-1]]
        i += jump

    print(f'#{Tc} {find_flag}')
