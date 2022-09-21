def brute_check(info, adj_dict, can_go, q):
    wolf = sum([info[i] for i in q])
    sheep = len(q) - wolf
    if sheep <= wolf:
        return sheep

    max_sheep = sheep
    for next_node in can_go:                # 중간 점검 통과한 서순은 뒷 서순도 추가
        can_go_next = can_go[:]
        can_go_next.remove(next_node)
        for node in adj_dict[next_node]:
            if node > 0:
                can_go_next.append(node)
        node_sheep = brute_check(info, adj_dict, can_go_next, q + [next_node])
        if node_sheep > max_sheep:
            max_sheep = node_sheep

    return max_sheep


def solution(info, edges):
    adj_dict = dict()                           # 이진트리 연결 딕셔너리 생성
    for node in range(len(info)):
        adj_dict[node] = [-1]               # 이진트리이므로 최대 2개의 자식 생성
    for line in edges:
        if adj_dict[line[0]][0] < 0:
            adj_dict[line[0]][0] = line[1]
        else:
            adj_dict[line[0]].append(line[1])

    answer = brute_check(info, adj_dict, adj_dict[0], [0])
    return answer


info = [0, 0]
edges = [[0, 1]]
print(solution(info, edges))