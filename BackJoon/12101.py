ans = list()

def make_eq(left, length, eq=''):
    global ans
    if len(ans) == length:
        return
    if left == 0:
        ans.append(eq[1:])
        return
    elif left >= 3:
        make_eq(left - 1, length, eq + '+1')
        make_eq(left - 2, length, eq + '+2')
        make_eq(left - 3, length, eq + '+3')
    elif left == 2:
        make_eq(left - 1, length, eq + '+1')
        make_eq(left - 2, length, eq + '+2')
    else:
        make_eq(left - 1, length, eq + '+1')


n, k = map(int, input().split())
make_eq(n, k)
if len(ans) < k:
    ans.append(-1)
print(ans[-1])
