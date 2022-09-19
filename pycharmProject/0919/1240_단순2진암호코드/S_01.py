import sys
sys.stdin = open('input.txt')
decode = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9',
}
T = int(input())

for Tc in range(1, T+1):                # 주어진 배열에서 코드위치 추출
    N, M = map(int, input().split())
    mat = [input() for _ in range(N)]
    for row in range(N):
        if '1' in mat[row]:
            for col in range(M-1 , 0, -1):
                if mat[row][col] == '1':
                    idx = col + 1
                    break
            break

    code = ''
    for x in range(8):                              # 배열에서 코드 추출
        code = decode[mat[row][idx-7: idx]] + code
        idx -= 7

    a = 0
    b = 0
    for i in range(4):                              # 코드 유효성 검사
        a += int(code[2 * i])
        b += int(code[2 * i + 1])
    valid = a*3 + b

    ans = 0
    if not valid % 10:                                # 코드 해석
        for i in code:
            ans += int(i)

    print(f'#{Tc} {ans}')
