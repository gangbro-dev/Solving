import sys
sys.stdin = open('input.txt')

T = int(input())
factor = [2, 3, 5, 7, 11]
for Tc in range(1, T+1):
    N = int(input())
    ans = ['#'+str(Tc)]
    for i in factor:
        cnt = 0
        while not N % i:
            N //= i
            cnt += 1
        ans.append(cnt)
    print(*ans)
