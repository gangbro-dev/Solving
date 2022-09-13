# import sys
# sys.stdin = open('sample_input.txt')
def inorder(start, order):                  # 중위순회 함수
    if ch[start]:                           # 자식이 있다면,
        inorder(ch[start][0], order)        # 재귀를 통해서 왼쪽 자식에 다시 시작
        order.append(start)                 # 부모를 order에 저장
        if len(ch[start]) > 1:              # 만약, 오른쪽 자식이 있다면
            inorder(ch[start][1], order)    # 재귀를 통해 오른쪽 자식에서 다시 시작
    else:
        order.append(start)                 # 자식이 없다면 바로 부모를 order에 저장하고, 함수 빠져나옴


for Tc in range(1, 11):
    N = int(input())
    # 숫자에 맞는 글자를 저장할 리스트. 번호 값은 1~N이므로 N+1개 만들어 둔다.
    # 기본값을 None으로 하여 만약 틀린 번호를 접근하면 에러가 발생한다.
    char = [None] * (N + 1)
    # 자식 리스트. 부모의 노드 번호 값을 이용해서 접근한다. 번호 값은 1~N이므로 N+1개 만들어 둔다.
    ch = [()] * (N + 1)
    for i in range(N):
        n, c, *child = input().split()      # 입력값을 언패킹을 통해서 받아온다
        n = int(n)                          # n 은 문자열이므로 정수로 변환
        char[n] = c                         # n 에 맞는 문자열 저장
        # child는 문자열을 가진 리스트로 받아진다. 이를 정수로 이루어진 튜플로 변환한다.
        child = tuple(map(int, child))
        ch[n] = child                       # 자식 리스트에 맞는 인덱스로 대입한다.

    order = []                              # 문자 순서를 번호로 저장할 리스트
    inorder(1, order)                       # 중위 순회 함수
    ans = ''                                # 정답을 저장할 문자열
    # 문자 순서 번호를 이용해서 맞는 문자에 순차적으로 접근하면서, 문자열을 더함
    for i in order:
        ans += char[i]

    print(f'#{Tc} {ans}')
