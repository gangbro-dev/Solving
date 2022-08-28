def switch_push(switch, a):
    if switch[a]:
        switch[a] = 0
    else:
        switch[a] = 1


switch_num = int(input())

switch = [-1] + list(map(int, input().split()))

student_num = int(input())

for _ in range(student_num):
    student = tuple(map(int, input().split()))
    if student[0] == 1:
        i = 1
        while (i * student[1]) <= switch_num:
            switch_push(switch, i * student[1])
            i += 1

    else:
        switch_push(switch, student[1])
        i = 1
        while student[1] + i <= switch_num and 0 < student[1] - i:
            if switch[student[1] + i] == switch[student[1] - i]:
                switch_push(switch, student[1] + i)
                switch_push(switch, student[1] - i)
            else:
                break
            i += 1
i = 1
while i <= switch_num:
    print(switch[i], end=' ')
    if not i % 20:
        print()
    i += 1
