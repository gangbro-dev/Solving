def check(subtree):
    l = len(subtree)

    if l == 1:
        return True

    center = l // 2

    if subtree[center] == '0':
        if '1' in subtree:
            return False
    else:
        return check(subtree[:center]) and check(subtree[center+1:])

    return True


def solution(numbers):
    bin_len = [1, 3, 7, 15, 31, 63]
    answer = []
    for idx in range(len(numbers)):
        bin_num = ''
        while numbers[idx]:
            bin_num = f'{numbers[idx] % 2}' + bin_num
            numbers[idx] //= 2

        l = len(bin_num)
        while l not in bin_len:
            bin_num = '0' + bin_num
            l = len(bin_num)

        if check(bin_num):
            answer.append(1)
        else:
            answer.append(0)
    return answer


print(solution([63, 111, 95]))