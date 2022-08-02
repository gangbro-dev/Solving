import sys
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
        light_diff.append('0')
    else:
        light_diff.append('1')

# case index 0 == '0'
for i in range(N):
    if True:
        pass


