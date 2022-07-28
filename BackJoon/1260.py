def DFS(graph_list, sol_list, start):
    for i in graph_list[start]:
        if not i in sol_list:
            sol_list.append(i)
            num = i
            DFS(graph_list, sol_list, num)
    return ' '.join(list(map(str, sol_list)))

def BFS(graph_list, sol_list, start):
    count = 1
    while True:
        for i in graph_list[start]:
            if not i in sol_list:
                sol_list.append(i)
        if len(sol_list) == graph_list['N'][0]:
            return ' '.join(list(map(str, sol_list)))
        else:
            start = count
            count += 1
                  
complete_set = set() # 탐색 완료한 정점 모음
setting_value = input() # 첫줄 그래프 정보 받음

N, M, start = map(int, setting_value.split())

conn_info = {'N' : [N]}

# 각 노드마다 연결정보를 conn_info 딕셔너리에 저장
for i in range(M):
    conn_value = list(map(int, input().split()))
    if conn_value[0] in conn_info:
        conn_info[conn_value[0]].append(conn_value[1])
    else:
        conn_info[conn_value[0]] = [conn_value[1]]
    if conn_value[1] in conn_info:
        conn_info[conn_value[1]].append(conn_value[0])
    else:
        conn_info[conn_value[1]] = [conn_value[0]]

for i in conn_info.keys(): # 각 노드별 연결정보 정렬
        conn_info[i].sort()

solution = [start]
#print(DFS(conn_info, solution, start))
solution = [start]
print(BFS(conn_info, solution, start))

