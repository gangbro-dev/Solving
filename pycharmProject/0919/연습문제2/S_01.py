T = int(input())

for Tc in range(1, T + 1):
    num = input()
    my_bin = ''
    for a in num:
        my_bin = my_bin + str(format(int(a, 16), '04b'))
    i = 0
    ans = 0
    for bit in my_bin:
        if bit == '1':
            ans += 2 ** (6 - i)
        i += 1
        if i > 6:
            i = 0
            print(ans, end=' ')
            ans = 0
    else:
        ans = ans // (2 ** (7 - i))
        print(ans, end=' ')
    print()
