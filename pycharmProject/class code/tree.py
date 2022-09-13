'''
정점 번호 1 ~ (E + 1)
입력 1 : 간선 수
입력 2 :간선마다 부모-자식 순으로 나열 해서 입력
4
1 2 1 3 3 4 3 5
'''


def find_root(V):
    for i in range(1, V+1):
        if par[i] == 0:
            return i


def preorder(n):    # 전위 순회
    if n:
        print(n)    #visit(n)
        preorder(ch1[n])
        preorder(ch2[n])


def inorder(n):     # 중위 순회
    if n:
        inorder(ch1[n])
        print(n)  # visit(n)
        inorder(ch2[n])


def postorder(n):   # 후위 순회
    if n:
        inorder(ch1[n])
        inorder(ch2[n])
        print(n)  # visit(n)


E = int(input())
arr = list(map(int, input().split()))
V = E + 1
# 부모를 인덱스로 자식 번호 저장 자식1번 자식2번(이진 트리)
ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)
# 부모 노드가 무엇인지 표현
par = [0] * (V + 1)
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    par[c] = p
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

root = 1
preorder(root)
inorder(root)
postorder(root)
find_root(4)


