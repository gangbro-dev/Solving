import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    my_str = input()
    check_brace = []
    check_flag = 0
    for i in my_str:
        # 괄호 열기 : 스택에 괄호종류 저장
        if i == '(' or i == '{' or i == '[':
            check_brace.append(i)
        # 괄호 닫기 : 스택에서 괄호 종류 확인. 틀리다면 break
        if i == ')' or i == '}' or i == ']':
            # 만약 스택이 비어있다면 틀린 괄호임
            if not check_brace:
                break
            if i == ')' and check_brace.pop() != '(':
                break
            elif i == '}' and check_brace.pop() != '{':
                break
            elif i == ']' and check_brace.pop() != '[':
                break
    else:
        if not check_brace:
            check_flag = 1

    print(f'#{Tc} {check_flag}')
