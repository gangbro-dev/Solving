#  솔루션 코드를 작성합니다.
import sys
sys.stdin=open('input.txt')

tc =int(input())
for test in range(tc):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result_list = []
    for y in range(N-M+1):
        for x in range(N-M+1):
            # 0,0 부터 2,2까지
            total = 0
            for i in range(M):
                for j in range(M):
                    total += arr[i+y][j+x]
            result_list.append(total)
    max_value = 0
    for i in result_list:
        if i > max_value:
            max_value = i
    print(f'#{test+1} {max_value}')
