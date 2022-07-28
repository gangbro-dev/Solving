def DFS(graph_dict, sol_list, start):
    for i in graph_dict[start]:
        if not i in sol_list:
            sol_list.append(i)
            num = i
            DFS(graph_dict, sol_list, num)
    return ' '.join(list(map(str, sol_list)))

def BFS(graph_dict, sol_list, start):
    cnt = 0
    backcnt = -1
    while len(sol_list) < graph_dict['N'][0]:
        if backcnt == cnt:
            break
        for i in graph_dict[sol_list[cnt]]:
            if i not in sol_list:
                sol_list.append(i)
        backcnt = len(sol_list)
        cnt += 1
        
        
    return ' '.join(list(map(str, sol_list)))
                  
complete_set = set() # 탐색 완료한 정점 모음
setting_value = input() # 첫줄 그래프 정보 받음

N, M, start = map(int, setting_value.split())

conn_info = {'N' : [N]}
conn_info[start] = []
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
print(DFS(conn_info, solution, start))
solution = [start]
print(BFS(conn_info, solution, start))
