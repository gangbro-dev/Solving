def top(idx):
    if idx == 0:
        return 5
    elif idx == 1:
        return 3
    elif idx == 2:
        return 4
    elif idx == 3:
        return 1
    elif idx == 4:
        return 2
    elif idx == 5:
        return 0


N = int(input())
dice = list()
for i in range(N):
    dice.append(list(map(int, input().split())))

max_cnt = 0
max_loss = 20000
for first_bottom in range(1, 7):
    cnt = 0
    loss = 0
    next_bottom = dice[0][top(dice[0].index(first_bottom))]

    if first_bottom * next_bottom == 30:
        cnt += 4
        loss += 2
    elif first_bottom == 6 or next_bottom == 6:
        cnt += 5
        loss += 1
    else:
        cnt += 6

    for i in range(1, N):
        this_bottom = next_bottom
        next_bottom = dice[i][top(dice[i].index(this_bottom))]
        if this_bottom * next_bottom == 30:
            cnt += 4
            loss += 2
        elif this_bottom == 6 or next_bottom == 6:
            cnt += 5
            loss += 1
        else:
            cnt += 6

        if loss >= max_loss:
            break
    else:
        max_cnt = max(max_cnt, cnt)
        max_loss = min(max_loss, loss)

print(max_cnt)
