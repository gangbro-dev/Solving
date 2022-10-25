def hanoi(height, start=1, end=3, spare=2):
    if height == 1:
        ans.append(f'{start} {end}')
    else:
        hanoi(height - 1, start, spare, end)
        ans.append(f'{start} {end}')
        hanoi(height - 1, spare, end, start)


N = int(input())
ans = list()
hanoi(N)
print(len(ans))
for i in ans:
    print(i)
