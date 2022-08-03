import sys

def switch_check(light_diff):
    # 예외케이스 N = 2이면 아래 반복문은 인덱스 에러가 나므로, 미리 체크한다.
    if N == 2:
        if light_diff[0] and light_diff[1]:
            return 1
        elif not light_diff[0] and not light_diff[1]:
            return 0
        else:
            return -1

    #case0와 case1에서 쓸 리스트 제작
    light_diff2 = light_diff[:]

    # case0
    # 만약, 0에서부터 N 까지의 index에서 0번 스위치를 누르지 않는다고 햇을 때, 0번 불에 영향을 미치는 것은 1번 뿐이므로
    # 0번 불을 바꿔야 하면 1번을 누르고, 아니면 누르지 않는 방식밖에 쓸 수 없다.
    # 이 과정 이후 1번 불을 바꿔야 하면, 다시 2번 스위치를 누르는 방법 밖에 남지 않는다.
    # 이 과정을 N번 스위치 까지 반복했을 때의 카운터 결과값이 case0의 해이다.
    # 만약 마지막 버튼을 눌렀을 때, 마지막 항이 False를 만들 수 없다면 case0는 불가능 이다.
    cnt = 0
    # i+1번 버튼을 눌렀을 때의 반복문+
    for i in range(N-2):
        if light_diff[i]:
            light_diff[i] = not light_diff[i]
            light_diff[i+1] = not light_diff[i+1]
            light_diff[i+2] = not light_diff[i+2]
            cnt += 1
    # 마지막 버튼은 맨 뒤 두 불에만 영향을 미치므로 따로 계산
    if light_diff[N-2]:
        cnt += 1
        light_diff[N-2] = not light_diff[N-2]
        light_diff[N-1] = not light_diff[N-1]
    # 마지막 항 검사
    if light_diff[N-1]:
        case0 = -1
    else:
        case0 = cnt

    # case1 0번 스위치를 누르고 시작하는 경우이다.
    # 나머지 결과값은 위와 같다.
    cnt = 0
    # 0번 스위치 누름
    light_diff2[0] = not light_diff2[0]
    light_diff2[1] = not light_diff2[1]
    cnt += 1
    # i+1번 버튼을 눌렀을 때의 반복문
    for i in range(N-2):
        if light_diff2[i]:
            light_diff2[i] = not light_diff2[i]
            light_diff2[i+1] = not light_diff2[i+1]
            light_diff2[i+2] = not light_diff2[i+2]
            cnt += 1
    # 마지막 버튼은 맨 뒤 두 불에만 영향을 미치므로 따로 계산
    if light_diff2[N-2]:
        cnt += 1
        light_diff2[N-2] = not light_diff2[N-2]
        light_diff2[N-1] = not light_diff2[N-1]
    # 마지막 항 검사
    if light_diff2[N-1]:
        case1 = -1
    else:
        case1 = cnt
    # 둘 중 가능한 경우를 출력
    # 만약, 둘 다 가능하면 그 중 작은 값을 출력
    if case0 < 0:
        return case1
    elif case1 < 0:
        return case0
    else:
        return min(case0, case1)

# input을 받아서 그 값을 N, origin_light, goal_light 에 저장
N = int(sys.stdin.readline())
line1 = sys.stdin.readline().strip()
line2 = sys.stdin.readline().strip()
origin_light = []
origin_light.extend(line1)
goal_light = []
goal_light.extend(line2)

# 시작과 끝이 다른 점만 추출해서 새로운 리스트에 저장
light_diff = []
for i in range(N):
    if origin_light[i] == goal_light[i]:
        light_diff.append(origin_light[i] == goal_light[i])
    else:
        light_diff.append(True)
    # light_diff.append(origin_light[i] != goal_light[i])
print(switch_check(light_diff))