import sys
input = sys.stdin

N = int(input())
tree = [[] for _ in range(N+1)]
for i in range(N):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# ????
