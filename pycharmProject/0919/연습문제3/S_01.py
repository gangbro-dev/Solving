decode = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9
}

T = int(input())

for Tc in range(1, T + 1):
    num = input()
    my_bin = ''
    for a in num:
        my_bin = my_bin + str(format(int(a, 16), '04b'))

    pattern = my_bin[0:6]
    i = 6
    while i < len(my_bin):
        if pattern in decode.keys():
            print(decode[pattern], end=' ')
            pattern = my_bin[i:i+6]
            i += 6
        else:
            pattern = pattern[1:] + my_bin[i]
            i += 1
    print()
