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
