def isright(string):
    stack = ['error']
    for i in string:
        if i == '(':
            stack.append('')
        elif i == ')':
            a = stack.pop()
            if a:
                return False
    return True


def wuv(w):
    if not w:
        return w

    left = right = 0
    for i in range(len(w)):
        if w[i] == '(':
            left += 1
        elif w[i] == ')':
            right += 1
        if left == right:
            u = w[:i + 1]
            v = w[i + 1:]
            break
    else:
        u = w
        v = ''

    if isright(u):
        u += wuv(v)
        return u
    else:
        edit = '('
        edit += wuv(v)
        edit += ')'
        for j in u[1:-1]:
            if j == '(':
                edit += ')'
            elif j == ')':
                edit += '('
        return edit


def solution(p):
    if isright(p):
        return p
    else:
        return wuv(p)
