import sys
sys.stdin = open('sample_input.txt')
# 인덱스를 N길이로 만들고, 그걸 이용해서 반복, 재귀로 들어갈 때마다, 선택한 인덱스 제거

def pick(mat, idx, value, row):         # 한 줄에서 어떤 원소를 선택할 지 정하는 함수
    global ans                          # 전체
    if row == len(mat):
        return sum(value)
    for i in idx:
        val = value[:]
        if ans < sum(val):              # 가지치기(최솟값보다 중간합이 큰 경우)
            return ans
        if i in idx:
            val.append(mat[row][i])
            min_sum = pick(mat, idx - {i,}, val, row+1)
            if ans > min_sum:
                ans = min_sum
    return ans

T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    idx = set(range(N))
    value = []
    ans = 9999999
    pick(mat, idx, value, 0)

    print(f'#{Tc} {ans}')