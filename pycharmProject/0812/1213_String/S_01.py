import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')


def searchstr(sts, wrd):                # 문장에서 특정 단어를 탐색하는 함수
    cnt = 0                             # 반환할 카운트 값
    for i in range(len(sts)):           # 문장의 길이 동안 단어 탐색
        if sts[i] == wrd[0]:            # 만약, 단어의 첫 글자를 찾으면
            k = 1
            for j in wrd[1:]:           # 단어의 나머지 글자 탐색
                if i+k >= len(sts):     # 만약 남은 단어 길이보다 남은 문장 글자 수가 작으면 끝냄
                    break
                if j == sts[i+k]:       # 만약, 그 다음 글자도 일치하면, 그 다음 글자를 찾음
                    k += 1
                else:                   # 만약, 글자가 일치하지 않으면 탈출
                    break
            else:                       # 만약 모든 글자가 일치해서 탈출하지 않았다면, 카운트
                cnt += 1
    return cnt


for _ in range(1, 11):
    T = int(input())
    wrd = input()
    sts = input()
    print(f'#{T} {searchstr(sts, wrd)}')
