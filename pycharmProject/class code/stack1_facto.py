def facto(n):
    if n <= 1:
        return 1
    else:
        return n * facto(n-1)

for i in range(21):
    print(i, facto(i))