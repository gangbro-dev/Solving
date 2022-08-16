import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

T = int(input())

for _ in range(T):
    Tc, N = input().split()
    num_list = list(input().split())
    cnt = {'ZRO': 0,                    # 각 문자열이 나온횟수를 측정하는 딕셔너리
           'ONE': 0,
           'TWO': 0,
           'THR': 0,
           'FOR': 0,
           'FIV': 0,
           'SIX': 0,
           'SVN': 0,
           'EGT': 0,
           'NIN': 0}
    for i in num_list:                  # 딕셔너리의 키 값이 곧 그 문자열이므로, 키를 이용해서 숫자를 세자
        cnt[i] += 1
    result = ''
    for i in cnt.keys():                # 딕셔너리의 키는 순서가 존재하므로, 그 순서를 이용해서 원하는 값을 사용한다.
        result = result + ((i + ' ') * cnt[i]) # 각 문자마다 공백을 붙여서, 위에서 센 개수만큼 반복해서 출력한다.

    print(f'{Tc}')
    print(f'{result}')
