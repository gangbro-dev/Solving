def solution(commands):
    answer = []
    table = [[None] * 51 for _ in range(51)]
    # 데이터가 있는 개별 셀들의 좌표
    valuable_cell = []
    # 병합 셀 데이터를 넣을 딕셔너리
    merge_dict = dict()
    # 병합 셀 데이터의 key 값
    merge_count = 0
    for command in commands:
        com, r, c, *data = command.split()
        if com == 'UPDATE':     # 수정
            # 셀에 새로운 데이터를 업데이트 하는 경우
            if data:
                r = int(r)
                c = int(c)
                # 병합 된 셀에 데이터를 업데이트 하는 경우
                if type(table[r][c]) is int:
                    merge_dict[table[r][c]][0] = data[0]
                    valuable_cell.append((r, c))
                # 일반 셀에 데이터를 업데이트 하는 경우
                else:
                    table[r][c] = data[0]
                    valuable_cell.append((r, c))
            # 데이터를 가진 셀을 찾아 바꾸기 하는 경우
            else:
                value1 = r
                value2 = c
                # 병합 셀을 모두 찾음
                for key in merge_dict.keys():
                    if merge_dict[key][0] == value1:
                        merge_dict[key][0] = value2
                # 데이터가 존재하는 개별 셀을 찾음
                for row, col in valuable_cell:
                    if table[row][col] == value1:
                        table[row][col] = value2
        elif com == 'MERGE':    # 셀 병합
            r1, c1 = int(r), int(c)
            r2, c2 = map(int, data)
            if (r1, c1) in valuable_cell:
                valuable_cell.remove((r1, c1))
            if (r2, c2) in valuable_cell:
                valuable_cell.remove((r2, c2))
            # 병합된 셀과 다른 셀을 병합할 경우
            if type(table[r1][c1]) is int:
                # 이미 병합되어 있는 두 셀인 경우
                if table[r1][c1] == table[r2][c2]:
                    pass
                # 병합된 셀과 다른 병합된 셀을 병합하는 경우
                elif type(table[r2][c2]) is int:
                    key = table[r2][c2]
                    past_data = merge_dict[table[r2][c2]][0]
                    for cell in merge_dict[table[r2][c2]][1:]:
                        row, col = cell
                        merge_dict[table[r1][c1]].append((row, col))
                        table[row][col] = table[r1][c1]
                    if not merge_dict[table[r1][c1]][0]:
                        merge_dict[table[r1][c1]][0] = past_data
                    del merge_dict[key]
                else:
                    past_data = table[r2][c2]
                    merge_dict[table[r1][c1]].append((r2, c2))
                    table[r2][c2] = table[r1][c1]
                    if not merge_dict[table[r1][c1]][0]:
                        merge_dict[table[r1][c1]][0] = past_data
            # 셀과 병합된 셀을 병합하는 경우
            elif type(table[r2][c2]) is int:
                merge_dict[table[r2][c2]].append((r1, c1))
                if table[r1][c1]:
                    merge_dict[table[r2][c2]][0] = table[r1][c1]
                table[r1][c1] = table[r2][c2]
            # 병합되지 않은 셀 끼리 병합할 경우
            else:
                merge_dict[merge_count] = [None, (r1, c1), (r2, c2)]
                if table[r1][c1]:
                    merge_dict[merge_count][0] = table[r1][c1]
                elif table[r2][c2]:
                    merge_dict[merge_count][0] = table[r2][c2]
                table[r1][c1], table[r2][c2] = merge_count, merge_count
                merge_count += 1

        elif com == 'UNMERGE':  # 셀 병합 해제
            r = int(r)
            c = int(c)
            # 병합셀이라면, 병합된 셀을 모두 분리하고, 모든 셀은 프로그램 실행 초기상태로 전환, 지정된 셀은 병합셀의 데이터를 가짐
            if table[r][c] in merge_dict.keys():
                past_merge_data = merge_dict[table[r][c]][0]
                key = table[r][c]
                for cell in merge_dict[table[r][c]][1:]:
                    row, col = cell
                    table[row][col] = None
                del merge_dict[key]
                table[r][c] = past_merge_data
                valuable_cell.append((r, c))
        elif com == 'PRINT':    # 출력
            r = int(r)
            c = int(c)
            # 셀 데이터가 문자열인 경우
            if type(table[r][c]) == str:
                answer.append(table[r][c])
            # 셀이 병합셀인 경우
            elif type(table[r][c]) == int:
                answer.append(merge_dict[table[r][c]][0])
            # 셀이 비어있는 경우
            else:
                answer.append('EMPTY')

    return answer
