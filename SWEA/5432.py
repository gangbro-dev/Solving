import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    steel_bar = input()
    stack = []
    laser_flag = 0
    cnt = 0
    for i in steel_bar:
        if i == '(':
            stack.append(i)
            laser_flag = 1
            cnt += 1
        elif i ==')':
            stack.pop()
            if laser_flag:
                cnt += len(stack) -1
            laser_flag = 0

    print(f'#{Tc} {cnt}')
