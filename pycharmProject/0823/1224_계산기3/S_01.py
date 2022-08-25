import sys
sys.stdin = open('input.txt')


def postfix_mod(eq):
    isp = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }
    stack = []
    postfix = []

    for elem in eq:
        if elem.isdecimal():
            postfix.append(elem)
        else:
            if elem == '(':
                stack.append(elem)
            elif elem == ')':
                while True:
                    if stack[-1] == '(':
                        stack.pop()
                        break
                    else:
                        postfix.append(stack.pop())
            else:
                while stack and isp[stack[-1]] >= isp[elem]:
                    postfix.append(stack.pop())
                stack.append(elem)
    else:
        while stack:
            postfix.append(stack.pop())

    return postfix


def split_mean(string):
    split_list = []
    temp = ''
    for char in string:
        if not char.isdecimal():
            if temp:
                split_list.append(temp)
                temp = ''
            split_list.append(char)
        else:
            temp += char
    else:
        if temp:
            split_list.append(temp)

    return split_list


for Tc in range(1, 11):
    N = int(input())
    equation = input()
    equ = postfix_mod(split_mean(equation))
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

    print(*stack)
