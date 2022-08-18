# 정점마다 연결된 간선을 정점마다 연결된 정점들로 변경
input = '1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7'
line = list(map(int, input.split(',')))
N = 7
# 연결정보를 저장할 리스트 선언. 1부터 7까지 존재하므로 0번 인덱스를 비워두고 사용하지 않음
graph = [[] for _ in range(N+1)]
for i in range(len(line)//2):
    graph[line[(2*i)]].append(line[(2*i)+1])
    graph[line[(2*i)+1]].append(line[(2*i)])
    # 낮은 숫자부터 방문하기 위해서 정렬
    graph[line[(2*i)]].sort()
    graph[line[(2 * i) + 1]].sort()

# dfs
v = 1                       # 시작점
visited = [False]*(N+1)     # visited 초기화
stack = [-1] * (N+1)        # stack 초기화
top = -1
visited[v] = True              # 시작점 방문 표시
visit_order = [v]
while True:
    for w in graph[v]:
        if not visited[w]:          # 방문하지 않은 인접 정점 w 가 존재하면
            top += 1                # 스택에 저장
            stack[top] = v
            v = w                   # 다음 정점으로 저장
            visited[w] = True       # 방문 표시
            visit_order.append(v)   # 순서 저장
            break
    else:                           # 방문하지 않은 인접 정점 w 가 존재하지 않으면
        if top != -1:               # 스택이 비어있지 않은 경우
            v = stack[top]
            top -= 1
        else:                       # 모든 스택이 비워지면
            break

print(*visit_order)
