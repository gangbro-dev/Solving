# 모든 경우 중에 최소합을 가지는 경우만 먼저 계산하면 되지 않을까
# -> 첫번째 경우부터 오답
# 사이계산에 순서를 적으면 순열로 연산 경우의 수를 표현할 수 있다
# 예를 들어
# 40, 30, 30, 50
#   \/  \/  \/
#    0   1   2
# 위와 같이 사이 계산마다 번호를 붙이면 그 번호의 순열 만큼의 경우의 수가 나온다
# 최대 500개의 숫자이므로, 순열인 500!의 경우의 수는 연산할 수 없다
# 어케하지
# 3개 부터 확장해서 한개씩 추가해볼까
# 40 30 30
# 1 0
# 40 30 30 50
# 0 2 1
# ?
# 2번 해보자
# 0 1
# 2 0 1
# 2 3 0 1
# 2 3 0 1 4
# 5 2 3 0 1 4
#
# 몬가.. 몬가 잇는데

# 폐기코드 1 남은 것들 중 비용 최솟값을 찾아서 사용
def combine_file(size_list):
    cost = 0
    while len(size_list) != 1:
        min_cost = 22222
        min_idx = -1
        for idx in range(len(size_list)-1):
            if size_list[idx] + size_list[idx+1] < min_cost:
                min_cost = size_list[idx] + size_list[idx+1]
                min_idx = idx
        cost += min_cost
        size_list = size_list[:min_idx] + [min_cost] + size_list[min_idx+2:]
    return cost


T = int(input())

for Tc in range(T):
    K = int(input())
    size_list = list(map(int, input().split()))

    ans = combine_file(size_list)
    print(ans)
