# 그래프 구조는 비선형적인 연결로 이루어진 자료구조입니다.
# 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요합니다.
# DFS는 깊이우선탐색 입니다.
v = 0
n = 10
graph = [ [1,2],
          [0,3,4],
          [0,4],
          [1,5],
          [3,4,6],
          [5],
          []]


def dfs(v, n):              # v = 시작점, n = 총 노드의 개수
    top = -1
    print(v)                # 방문점 출력
    visited[v] = True       # 출발점 처리
    top += 1
    stack[top] = v
    while True:
        for w in graph[v]:              # if (v의 인접 정점 중 방문 안한 정점 w가 있으면
            if visited[w] == False:
                top += 1                # push(v)
                stack[top] = v
                v = w                   # v <- w (w 에 방문)
                print(v)                # 방문점 출력
                visited[w] = 1
                break
        else:                           # w가 없으면
            if top != -1:               # 스택이 남아있는 경우
                v = stack[top]          # pop
                top -= 1
            else:                       # 스택이 비어있으면
                break                   #


visited = [False] * n       # visited 생성
stack = [0] * n         # stack 생성
dfs(0, 7)
