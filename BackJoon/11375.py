# 1번안 리스트
# b가 a보다 무거움
# 그럼 a랑 비교했던 다른 샘플에 모두 b와 연계되는 정보 생성해야함
# 전수조사해야하는데 비용이 무거움 -> 기각
# 2번안 딕셔너리
# 이게나을듯?
from sys import stdin

input = stdin.readline

# 메모리초과
def 연계정보생성(b, a, w, results):
    # 연계정보 생성
    # b셋 안에 c가 있음 -> 이미 b와 c의 차이값이 있음 -> a c의 차잇값 구할 수 있다.
    for c in results[b]:
        # a와 c 사이에 차잇값이 없다면,
        if c not in results[a]:
            results[c][a] = results[c][b] + w
            results[a][c] = -results[c][a]

while True:
    Tc = list(map(int, input().split()))
    if Tc[0]:
        results = [dict() for _ in range(Tc[0]+1)]
        for i in range(Tc[1]):
            test = list(input().split())
            if test[0] == '!':
                a, b, w = map(int, test[1:])
                # b에 a에 관련된 정보 넣기
                results[b][a] = w
                # a 에 b에 관련된 정보 넣기
                results[a][b] = -w
                연계정보생성(b, a, w, results)
                연계정보생성(a, b, -w, results)
            else:
                a, b = map(int, test[1:])
                if a in results[b].keys():
                    print(results[b][a])
                else:
                    print("UNKNOWN")
    else:
        break
# 도원교수님s -> 재귀로 찾아가면서 무게를 더해서 교수님께 대답하자

# # Union&Find문제라는걸 알았음
# # 특정 원소가 속한 집합을 찾기
# def find(x):
#     # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
#     if parent[x] != x:
#         return find(parent[x])
#     return x
#
#
# # 두 원소가 속한 집합을 합치기
# def union(a, b):
#     a = find(a)
#     b = find(b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
#
# while True:
#     v, e = list(map(int, input().split()))
#     if v:
#         parent = [0] * (v + 1) # 부모 테이블 초기화하기
#         # 부모 테이블상에서, 부모를 자기 자신으로 초기화
#         for i in range(1, v + 1):
#             parent[i] = i
#     else:
#         break
#
# # 부모 테이블상에서, 부모를 자기 자신으로 초기화
# for i in range(1, v + 1):
#     parent[i] = i