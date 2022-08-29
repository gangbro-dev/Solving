K = int(input())
field = list()

long_x = 0
max_x = 0
long_y = 0
max_y = 0
for idx in range(6):
    field.append(tuple(map(int, input().split())))
    if field[idx][0] < 3 and max_x < field[idx][1]:
        long_x = idx
        max_x = field[idx][1]
    elif field[idx][0] >= 3 and max_y < field[idx][1]:
        long_y = idx
        max_y = field[idx][1]

if (long_x-1) % 6 == long_y:
    ans = field[long_y][1] * field[long_x][1]
    ans -= field[(long_y - 2) % 6][1] * field[(long_x + 2) % 6][1]
else:
    ans = field[long_y][1] * field[long_x][1]
    ans -= field[(long_x - 2) % 6][1] * field[(long_y + 2) % 6][1]

ans *= K

print(ans)
