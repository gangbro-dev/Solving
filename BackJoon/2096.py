import sys
input = sys.stdin.readline

N = int(input())
# DP. 에러 방지용 초기값 설정
MIN = (0, 0, 0,)
MAX = (0, 0, 0,)
# input 받으면서 각 DP실행
for _ in range(N):
    now = tuple(map(int, input().split()))
    MIN = (
        min(MIN[0] + now[0], MIN[1] + now[0]),
        min(MIN[0] + now[1], MIN[1] + now[1], MIN[2] + now[1]),
        min(MIN[1] + now[2], MIN[2] + now[2]),)
    MAX = (
        max(MAX[0] + now[0], MAX[1] + now[0]),
        max(MAX[0] + now[1], MAX[1] + now[1], MAX[2] + now[1]),
        max(MAX[1] + now[2], MAX[2] + now[2]),)

print(max(MAX), min(MIN))