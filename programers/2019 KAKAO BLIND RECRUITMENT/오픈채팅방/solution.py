def solution(record):
    info = dict()
    order = list()
    for rec in record:
        command, id, *nickname = rec.split()
        if command == 'Enter':
            info[id] = nickname[0]
            order.append((True, id))
        elif command == 'Leave':
            order.append((False, id))
        elif command == 'Change':
            info[id] = nickname[0]

    answer = []
    for o in order:
        if o[0]:
            answer.append(info[o[1]] + "님이 들어왔습니다.")
        else:
            answer.append(info[o[1]] + "님이 나갔습니다.")
    return answer
