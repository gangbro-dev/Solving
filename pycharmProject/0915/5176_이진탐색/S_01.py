import sys
sys.stdin = open('sample_input.txt')

def set_tree(tree, node):
    global cnt
    N = len(tree)
    if node*2 < N:
        set_tree(tree, node*2)
    tree[node] += cnt
    cnt += 1
    if node*2 + 1 < N:
        set_tree(tree, node*2 + 1)


T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    binary_tree = [0] * (N+1)
    cnt = 1
    set_tree(binary_tree, 1)
    print(f'#{Tc} {binary_tree[1]} {binary_tree[N//2]}')
