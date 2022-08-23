import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    equ = list(input().split())
    stack = []

    print(f'#{Tc}', end=' ')
    for char in equ:
        if char.isdecimal():
            stack.append(int(char))
        else:
            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
            else:
                print('error')
                break
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a // b)
    print(stack[0])
