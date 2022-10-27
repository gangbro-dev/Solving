import sys
input = sys.stdin.readline

N, M = map(int, input().split())

for i in range(1, N+1):
    input()

color_cnt = [0] * 3
for i in range(M):
    a = input().rstrip()
    if a[-1] == 'R':
        color_cnt[1] += 1
    elif a[-1] == 'B':
        color_cnt[2] += 1
    else:
        color_cnt[0] += 1

if color_cnt[1] > color_cnt[2]:
    print("jhnah917")
elif color_cnt[1] == color_cnt[2]:
    if color_cnt[0] % 2:
        print("jhnah917")
    else:
        print("jhnan917")
else:
    print("jhnan917")
