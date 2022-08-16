#  솔루션 코드를 작성합니다.
import sys

sys.stdin = open('input.txt')


def palin(word):
    if word == word[::-1]:
        return True
    else:
        return False


for test in range(1, 11):
    tc = int(input())
    arr = [input() for _ in range(100)]  # 가로 탐색
    arr_h = [''.join(i) for i in zip(*arr)]  # 세로 탐색
    max_length = 1

    for x in range(100, 1, -1):
        for i in range(len(arr)):
            for j in range(len(arr) - x + 1):
                if palin(arr[i][j:j + x]) == True:
                    max_length = max(x, max_length)

                elif palin(arr_h[i][j:j + x]) == True:
                    max_length = max(x, max_length)

    print(f'#{test} {max_length}')
