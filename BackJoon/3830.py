# from sys import stdin
#
# input = stdin.readline
#
# # 메모리초과
# def 연계정보생성(b, a, w, results):
#     # 연계정보 생성
#     # b셋 안에 c가 있음 -> 이미 b와 c의 차이값이 있음 -> a c의 차잇값 구할 수 있다.
#     for c in results[b]:
#         # a와 c 사이에 차잇값이 없다면,
#         if c not in results[a]:
#             results[c][a] = results[c][b] + w
#             results[a][c] = -results[c][a]
#
# while True:
#     Tc = list(map(int, input().split()))
#     if Tc[0]:
#         results = [dict() for _ in range(Tc[0]+1)]
#         for i in range(Tc[1]):
#             test = list(input().split())
#             if test[0] == '!':
#                 a, b, w = map(int, test[1:])
#                 # b에 a에 관련된 정보 넣기
#                 results[b][a] = w
#                 # a 에 b에 관련된 정보 넣기
#                 results[a][b] = -w
#                 연계정보생성(b, a, w, results)
#                 연계정보생성(a, b, -w, results)
#             else:
#                 a, b = map(int, test[1:])
#                 if a in results[b].keys():
#                     print(results[b][a])
#                 else:
#                     print("UNKNOWN")
#     else:
#         break

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(node):
    if p[node] == node:
        return node
    else:
        n = find(p[node])
        val[node] += val[p[node]]
        p[node] = n
        return p[node]


def union(a, b, w):
    roota = find(a)
    rootb = find(b)

    if roota == rootb:
        return
    else:
        val[rootb] = val[a] - val[b] + w
        p[rootb] = roota
        return


while True:
    Tc = list(map(int, input().split()))
    if Tc[0]:
        p = [i for i in range(Tc[0] + 1)]
        val = [0] * (Tc[0] + 1)
        for i in range(Tc[1]):
            test = list(input().split())
            if test[0] == '!':
                a, b, w = map(int, test[1:])
                union(a, b, w)
            else:
                a, b = map(int, test[1:])
                if find(a) == find(b):
                    print(val[b] - val[a])
                else:
                    print("UNKNOWN")
    else:
        break
