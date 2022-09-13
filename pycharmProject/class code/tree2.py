def pre(n):
    if n <= size:
        if tree[n]:
            print(tree[n], end=' ')
        pre(2*n)
        pre(2*n + 1)


def inor(n):
    if n <= size:
        inor(2*n)
        if tree[n]:
            print(tree[n], end=' ')
        inor(2*n + 1)


def post(n):
    if n <= size:
        post(2*n)
        post(2*n + 1)
        if tree[n]:
            print(tree[n], end=' ')


tree = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', None, None, 'K', 'L', 'M']
size = len(tree) - 1
pre(1)
print()
inor(1)
print()
post(1)
