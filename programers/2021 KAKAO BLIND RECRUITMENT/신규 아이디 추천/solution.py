def solution(new_id):
    # 1
    new_id = new_id.lower()

    # 2
    del_list = []
    for i in new_id:
        if i.isalnum() or i in '-_.':
            pass
        else:
            del_list.append(i)
    for i in del_list:
        new_id = new_id.replace(i, '')

    # 3
    new_new_id = new_id
    new_new_id = new_new_id.replace('..', '.')
    while new_new_id != new_id:
        new_id = new_new_id
        new_new_id = new_new_id.replace('..', '.')

    # 4
    if new_id[0] == '.':
        new_id = new_id[1:]
    if new_id[-1:] == '.':
        new_id = new_id[:-1]

    # 5
    if not new_id:
        new_id += 'a'

    # 6
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # 7
    while len(new_id) < 3:
        new_id += new_id[-1]

    answer = new_id

    return answer


id = 	"z-+.^."
print(solution(id))