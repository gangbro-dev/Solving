import sys
sys.stdin = open('sample_input.txt')


def merge_sort(m):
    global cnt
    if len(m) == 1:
        return m

    mid = len(m) // 2
    left = merge_sort(m[:mid])
    right = merge_sort(m[mid:])

    if max(left) > max(right):
        cnt += 1

    result = list()

    l = h = 0

    while l < len(left) and h < len(right):
        if left[l] < right[h]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[h])
            h += 1
    result += left[l:]
    result += right[h:]
    return result


T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    cnt = 0

    L = list(map(int, input().split()))

    ans = merge_sort(L)[N//2]

    print(f'#{Tc} {ans} {cnt}')
