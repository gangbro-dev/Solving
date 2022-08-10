def fibo(n):
    l_fibo = [0, 1]
    i = 0
    while True:
        if i == n:
            return l_fibo[i]
        if i > 0:
            l_fibo.append(l_fibo[i]+l_fibo[i-1])
        i+=1
                

def count_fibo(n):
    if n == 0:
        a = 1
        b = 0
    elif n == 1:
        a = 0
        b = 1
    else:
        a = fibo(n-1)
        b = fibo(n-2) + a
    print(f"{a} {b}")

T = int(input())
for i in range(T):
    N = int(input())
    count_fibo(N)