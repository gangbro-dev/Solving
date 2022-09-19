import sys
sys.stdin = open('input.txt')


def calculation(tree, values, node=1):
    if tree[node]:
        for n in tree[node]:
            calculation(tree, values, n)
        if values[node] == '+':
            values[node] = values[tree[node][0]] + values[tree[node][1]]
        elif values[node] == '-':
            values[node] = values[tree[node][0]] - values[tree[node][1]]
        elif values[node] == '*':
            values[node] = values[tree[node][0]] * values[tree[node][1]]
        elif values[node] == '/':
            values[node] = values[tree[node][0]] // values[tree[node][1]]

    return values[node]


T = 10

for Tc in range(1, T+1):
    N = int(input())
    values = [0] * (N+1)
    adj_graph = [[] for _ in range(N+1)]

    for _ in range(N):
        node, value, *ch = input().split()
        node = int(node)
        if value.isdigit():
            value = int(value)
            values[node] = value
        else:
            values[node] = value
            ch = list(map(int, ch))
            adj_graph[node].extend(ch)

    print(f'#{Tc} {calculation(adj_graph, values)}')
