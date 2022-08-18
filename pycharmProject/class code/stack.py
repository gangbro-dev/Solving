stackSize = 10      # stack 크기
stack = [0] * stackSize
top = -1            # top 초기값은 -1


def push(a, top):        # push 함수
    top += 1
    if top <= stackSize:
        return -1   # overflow_error
    else:
        stack[top] = a


def pop(top):
    top -= 1
    if top < 0:
        return -1   # underflow_error
    else:
        return stack[top+1]


push(1, top)
push(2, top)
push(3, top)
print(pop(top))
print(pop(top))
print(pop(top))
