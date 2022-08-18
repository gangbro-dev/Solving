import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for Tc in range(1, T+1):
    n = int(input())
    N = n//10           # 가로길이를 이용하기 쉽게 10으로 나눈다
    paper = [1, 1]      # 점화식을 이용하기 위한 초기값
    for i in range(1, N):
        paper.append(paper[i] + 2*paper[i-1])   # 점화식

    print(f'#{Tc} {paper[N]}')
