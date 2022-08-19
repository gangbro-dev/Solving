import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    input_list = [[] for _ in range(5)]
    for i in range(5):
        input_str = input()
        input_list[i].extend(input_str)
        while len(input_list[i]) < 15:
            input_list[i].append('')
    ans = ''
    for column in range(15):
        for row in range(5):
            ans += input_list[row][column]

    print(f'#{Tc} {ans}')