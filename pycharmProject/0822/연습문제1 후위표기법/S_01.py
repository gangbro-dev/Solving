import sys
sys.stdin = open('sample_input.txt')


def postfix_mod(eq):    # 리스트 원소들을 이용해서 후위표기법으로 변환
    isp = {     # 우선순위 저장
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }
    stack = []  # 스택
    postfix = []    # 후위표기법으로 변환한 순서대로 저장된 리스트

    for elem in eq:                 # 모든 리스트 원소들에 대해서
        if elem.isdecimal():        # 원소가 숫자로 이루어진 문자열이라면
            postfix.append(elem)    # 후위표기법 리스트에 저장
        else:                       # 아니라면(기호라면)
            if elem == '(':         # 여는 괄호이면
                stack.append(elem)  # 스택에 저장
            elif elem == ')':       # 닫는괄호라면
                while True:         # 스택에서 여는 괄호가 나올때까지 모두 팝 해서 후위표기법 리스트에 저장
                    if stack[-1] == '(':
                        stack.pop()
                        break
                    else:
                        postfix.append(stack.pop())
            else:                   # 다른 기호(연산기호)라면
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


T = int(input())

for Tc in range(1, T+1):
    equation = input()
    equ_list = split_mean(equation)

    print(f'#{Tc} {"".join(postfix_mod(equ_list))}')
