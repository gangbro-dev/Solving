adj_dict = dict()
line = list(map(int, input().split()))
for node in line:
    adj_dict[node] = []
for i in range(len(line)//2):
    adj_dict[line[2 * i]].append(line[2 * i + 1])
    adj_dict[line[2 * i + 1]].append(line[2 * i])

stack = [1]
visited = [0] * 10

while stack:
    now = stack.pop()
    if visited[now]:
        continue
    else:
        visited[now] = 1
        print(now, end=' ')
    for node in adj_dict[now]:
        if not visited[node]:
            stack.append(node)

print()
