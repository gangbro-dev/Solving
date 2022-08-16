def itoa(a):
    result = ''
    while a > 0:
        i = a % 10
        a = a // 10
        result = chr(ord('0') + i) + result

    return result


a = 123456
b = itoa(a)
print(b)
print(type(b))
