import sys
sys.stdin = open('sample_input.txt')

T = int(input())


for x in range(1, T+1):
    N = input()
    Number_count = [0]*10 # 들어오는 카드는 1자리 정수 -> 0-9의 값으로 표현된다.
    cards = input()
    for i in cards:
        Number_count[int(i)] += 1 # 카드문자열의 문자 하나 하나를 인트로 바꿔서 그 값의 인덱스에 +1
    max_num = 0
    max_num_idx = 0
    for i in range(10): # 가장 많은값을 찾는다.
        if Number_count[i] >= max_num:
            max_num = Number_count[i]
            max_num_idx = i

    print(f'#{x} {max_num_idx} {max_num}')
