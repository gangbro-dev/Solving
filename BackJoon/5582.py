A = input()
B = input()
setA = set()
setB = set()
for i in A:
    setA.add(i)
for i in B:
    setB.add(i)

check_set = setA & setB

if not len(check_set):
    print(0)
else:
    possible_set = set()
    conti_cnt = 0
    for i in range(len(A)):
        if A[i] in check_set:
            conti_cnt += 1
            possible_set.add(A[i])
            for j in range(conti_cnt):
                possible_set.add(A[i-j:i+1])
        else:
            conti_cnt = 0

    possible_list = list(possible_set)
    possible_list.sort(key=len, reverse=True)
    ans = 1

    for i in possible_list:
        if i in B:
            ans = len(i)
            break

    print(ans)
