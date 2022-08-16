import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    my_string, my_macro = input().split()
    S = len(my_string)
    M = len(my_macro)
    macro_count = len(my_string.split(my_macro))
    # 총 타이핑 = 문자열의 길이 - (매크로 문자열 - 1) * (매크로 문자열로 쓸 수 있는 구간의 개수)
    # 매크로 문자열 또한 1타를 사용하므로 (매크로 문자열 - 1) * (매크로 문자열로 쓸 수 있는 구간의 개수) 이다.
    print(f'#{Tc} {S - ((M-1)*(len(my_string.split(my_macro))-1))}')
