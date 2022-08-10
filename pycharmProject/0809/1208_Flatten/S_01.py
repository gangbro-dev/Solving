import sys
sys.stdin = open('input.txt')

for x in range(10):
    Dump = int(input())
    count = 0
    Box_Tall = list(map(int, input().split()))

    for i in range(Dump):
        max_idx = 0
        min_idx = 0
        for j in range(100): # 인덱스를 이용해서 최대 최소 값의 인덱스를 찾는다.
            if Box_Tall[j] < Box_Tall[min_idx]:
                min_idx = j
            if Box_Tall[j] > Box_Tall[max_idx]:
                max_idx = j
            if Box_Tall[max_idx] - Box_Tall[min_idx] < 2:
                break

        Box_Tall[max_idx] -= 1 # 최대값에 -1
        Box_Tall[min_idx] += 1 # 최소값에 +1

    max_tall = Box_Tall[0]
    min_tall = Box_Tall[0]
    for j in range(100):
        if Box_Tall[j] < min_tall: # 최대값 찾기
            min_tall = Box_Tall[j]
        if Box_Tall[j] > max_tall: # 최소값 찾기
            max_tall = Box_Tall[j]

    print(f'#{x+1} {max_tall - min_tall}')
