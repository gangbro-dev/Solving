# 1자리 암호 => 바로 해석하면 됨
# 2자리 암호 => 무조건 1과 2로 시작하면서 나타남 뒤에 0이 나오면 무조건 2자리 암호임
# 해석 불가 => 첫자리와 3~9뒤에 나오는 0으로 나타남
# 개수를 새서 구간을 분리하고, 구간마다 피보나치 수열임

# 0이 나오면 앞자리랑 무조건 묶음 그러므로 가짓수가 늘어나지 않음
# => 1, 2가 나오면 앞자리에 따라 달라짐 => 구간에 1을 뺀다(강제로 묶임. 나눌 수 없음)
# => 처음 0이 나오거나 3 ~ 9 가 나오면 에러임

# 1, 2가 나오면 구간이 연장됨

# 3 ~ 9 가 나오면 앞자리에 따라 달라짐
# => 1 라면 구간에 +1을 하고 구간 종료
# => 2 라면 숫자에 따라 달라짐
#   => 3 ~ 6 이라면 구간에 +1을 하고 구간 종료 (구간을 더함. 나눌 수도, 나누지 않을 수도 있음)
#   => 7 ~ 9 라면 구간을 더하지 않고 구간 종료 (구간을 더하지 않음. 독립적인 숫자 하나가 추가된 것)
# => 0, 3 ~ 9 라면 구간이 이어지지 않으므로 가짓 수에 영향을 주지 않음
def fibo(n):
    global FIBO
    while True:
        if len(FIBO) > n:
            return FIBO[n]
        else:
            FIBO.append(FIBO[-1] + FIBO[-2])


FIBO = [1, 1]
pwd = input()
count = 0
ans = 1
last = None
for i in pwd:
    if not int(i):
        if not count:
            ans = 0
            break
        else:
            ans *= fibo(count - 1)
            count = 0
            last = None
    elif int(i) < 3:
        count += 1
        last = int(i)
    else:
        if count:
            if last == 2:
                if int(i) > 6:
                    ans *= fibo(count)
                    count = 0
                    last = None
                    continue
            ans *= fibo(count + 1)
            count = 0
            last = None
else:
    if count:
        ans *= fibo(count)
        count = 0

print(ans % 1000000)
