import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):  # 입력받은 간선정보를 이용해서 그래프 생성
        start, end = map(int, input().split())
        graph[start].append(end)
    S, G = map(int, input().split())

    stack = [S]                 # 방문순서를 저장할 스택
    visited = [False] * (V+1)   # 방문 여부를 저장
    visited[S] = True           # 출발점 방문 설정
    flag = 1
    # dfs
    while flag:
        if stack[-1] != G:      # 만약, 현재 방문노드가 도착점이 아니라면,
            for i in graph[stack.pop()]:
                if not visited[i]:  # 방문하지 않은 현재 노드와 연결된 노드들을 스택에 저장
                    stack.append(i)
        else:
            break
        if not stack:           # 모든 스택을 사용해서 더 이상 방문할 노드가 없다면
            flag = 0

    print(f'#{Tc} {flag}')
