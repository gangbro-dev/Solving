import sys
sys.stdin = open('input.txt')

for Tc in range(1, 11):
    T, my_str = input().split()

    cnt = True
    while cnt:
        cnt = False  # 반복문자 지우기가 실행됬는지 확인
        i = 1
        while i < len(my_str):
            if my_str[i] == my_str[i-1]:                # 반복문자가 있는지 확인
                my_str = my_str[:i-1] + my_str[i+1:]    # 반복문자가 있다면, 그 문자들을 제거
                cnt = True
                i -= 2                                  # 반복문자 직전문자부터 확인
            i += 1

    print(f'#{Tc} {my_str}')
