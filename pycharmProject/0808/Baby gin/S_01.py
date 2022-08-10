import sys
sys.stdin = open('input.txt')

T = int(input())


for x in range(1, T+1):
    Number_count = [0]*10
    cards = input()
    for i in cards:
        Number_count[int(i)] += 1
    count = 0
    # Triplet 체크
    for i in range(10):
        while Number_count[i] > 2:
            Number_count[i] -= 3
            count += 1
    # run 체크
    for i in range(8):
        while Number_count[i] and Number_count[i+1] and Number_count[i+2]:
            Number_count[i] -= 1
            Number_count[i+1] -= 1
            Number_count[i+2] -= 1
            count += 1

    if count == 2:
        babygin = 1
    else:
        babygin = 0

    print(f'#{x} {babygin}')