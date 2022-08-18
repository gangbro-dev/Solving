stackSize = 10      # stack 크기
stack = [0] * stackSize
top = -1            # top 초기값은 -1


def push(a):        # push 함수
    top += 1
    if top <= stackSize:
        return
    else:
        stack[top] = a


def pop():
    top -= 1
    if top < -1:
        return
    else:
        return stack[top+1]


push(1)
push(2)
push(3)
