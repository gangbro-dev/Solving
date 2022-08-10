import sys
sys.stdin = open('input.txt')

T = int(input())   #10:34

for t in range(1, T+1):
    K, N, M = map(int, input().split())
    mli = [0]*(N+1)                          #충전소 위치 (0, 1)
    Mli = list(map(int, input().split()))    #충전소 위치
    ch = 0                                   #충전횟수
    go = K                                   #연료통
    hu = 0                                   #충전소 지나는 날
    for m in Mli:
        mli[m] = 1
    Mli.append(N)

    for n in range(1, N+1):
        if mli[n] == 0:                     #충전소 없으면 연료 한개 out
            go -= 1
        elif mli[n] == 1:                   #충전소 있으면 연료 한개쓰고
            go -= 1
            if go < 0:
                ch = 0
                break
            if go >= Mli[hu+1] - Mli[hu]:  #다음 충전소까지 갈 수 있으면 충전소 횟수세고
                hu += 1
            else:                            #go < Mli[i+1] - Mli[i]   없으면 충전하시오
                go = K
                ch += 1
                hu += 1

    print(f'#{t} {ch}')