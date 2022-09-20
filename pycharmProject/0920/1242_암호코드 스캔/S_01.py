import sys
sys.stdin = open('sample_input.txt')

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
    mat = []
    for _ in range(N):
        string = input().strip().rstrip('0')
        if string and string not in mat:
            mat.append(string)
    code_set = list()
    for row in mat:
        if row:                                                # 16진 암호 2진으로 변경
            bin_code = ''
            for i in row:
                bin_code += format(int(i, 16), '04b')

            temp = bin_code.rstrip('0')
            while temp:
                ratio = 1                                               # 2진암호 배율 찾기
                temp3 = temp[-56*ratio:]
                while True:
                    check1 = '0' + ('1' * ratio) + '0'
                    check2 = '1' + ('0' * ratio) + '1'
                    if check1 in temp3 or check2 in temp3:
                        break
                    ratio += 1
                temp2 = temp[-56*ratio::ratio]
                if temp2 not in code_set:
                    code_set.append(temp2)      # 2진암호 추출
                temp = temp[:-56*ratio]
                temp = temp.rstrip('0')
    ans = 0
    n = 0
    for raw_code in code_set:
        code = ''
        idx = 56
        for x in range(8):                              # 배열에서 코드 추출
            code = decode[raw_code[idx-7: idx]] + code
            idx -= 7
        n += 1
        a = 0
        b = 0
        for i in range(4):                              # 코드 유효성 검사
            a += int(code[2 * i])
            b += int(code[2 * i + 1])
        valid = a*3 + b

        if not valid % 10:                                # 코드 해석
            for i in code:
                ans += int(i)

    print(f'#{Tc} {ans}')
