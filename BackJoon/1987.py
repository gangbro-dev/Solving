def dfs(this_matrix, this_path_list, start, last_return):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    x, y = start
    path_list_now = this_path_list[:]
    path_list_now.append(this_matrix[y][x])
    max_path = max(len(path_list_now), last_return)
    for i in range(4):
        # 인덱스 이내인가
        if 0 <= x + dx[i] < C and 0 <= y + dy[i] < R:
            # 지나온 알파벳이 있는 칸인가
            if this_matrix[y + dy[i]][x + dx[i]] not in path_list_now:
                max_path = max(max_path, dfs(this_matrix, path_list_now, (x + dx[i], y + dy[i]), max_path))

    return max_path


R, C = map(int, input().split())

matrix = []

for row in range(R):
    matrix.append([])
    for j in input():
        matrix[-1].append(j)

path_list = []
print(dfs(matrix, path_list, (0, 0), 0))
