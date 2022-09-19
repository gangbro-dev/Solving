T = int(input())

for Tc in range(1, T + 1):
    num = input()
    i = 0
    ans = 0
    for bit in num:
        if bit == '1':
            ans += 2**(6-i)
        i += 1
        if i > 6:
            i = 0
            print(ans, end=' ')
            ans = 0
    print()
