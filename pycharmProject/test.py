num = input()

temp = format(int(num, 2), '07b')

print(temp)
print(format(int(num, 2) ^ 0b1111111, '07b'))
