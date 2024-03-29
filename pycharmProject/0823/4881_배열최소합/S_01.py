import sys
sys.stdin = open('sample_input.txt')
# 인덱스를 선택한 줄의 수로 만들고, 인덱스가 포함된 반복문에서는 내부 코드를 스킵

def pick(mat, idx, value, row):         # 한 줄에서 어떤 원소를 선택할 지 정하는 함수
    global ans                          # 전체
    if row == len(mat):
        return sum(value)
    for i in range(len(mat[row])):
        index = idx.copy()
        val = value[:]
        if ans < sum(val):              # 가지치기(최솟값보다 중간합이 큰 경우)
            return ans
        if i not in index:
            index.add(i)
            val.append(mat[row][i])
            min_sum = pick(mat, index, val, row+1)
            if ans > min_sum:
                ans = min_sum
    return ans

T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    idx = set()
    value = []
    ans = 9999999
    pick(mat, idx, value, 0)

    print(f'#{Tc} {ans}')