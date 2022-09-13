import math

ball_size = 5.71


# 점 두개가 x축과 이루는 각
def start_end_point_angle(start_point, end_point): # (y,x)의 튜플 2개 입력
    dx = end_point[1] - start_point[1]
    dy = end_point[0] - start_point[0]
    if dx:
        return math.atan2(dy, dx)
    else:
        return 0


# 목적구에 공 치는 위치
def hit_ball_point(hit_ball, target_angle):
    x = hit_ball[1]-(ball_size * math.cos(target_angle))
    y = hit_ball[0]-(ball_size * math.sin(target_angle))

    return tuple(y, x)


# 1번점과 2번점 사이에 방해물 체크크
def straight_point_flag(start_point, end_point, point_list):

    a = end_point[0] - start_point[0]
    b = start_point[1] - end_point[1]
    c = - ((a * start_point[1]) + (b * start_point[0]))

    min_x = min(start_point[1], end_point[1])
    max_x = max(start_point[1], end_point[1])
    min_y = min(start_point[0], end_point[0])
    max_y = max(start_point[0], end_point[0])
    flag = True
    for point in point_list:
        if min_y - ball_size < point[0] < max_y + ball_size and \
           min_x - ball_size < point[1] < max_x + ball_size:
            continue
        else:
            distance = abs(a * point[1] + b * point[0] + c) / math.sqrt((a ** 2) + (b ** 2))
            if distance < ball_size / 2:
                flag = False

    return flag



ball = [(0, 0) * 8]

table_center = {(127, 67.5),}
hole_position = [(-124, -64.5), (0, -64.5), (124, -64.5), (-124, 64.5), (0, 64.5), (124, 64.5),]
holes = list()
for table in table_center:
    for hole in hole_position:
        holes.append((table[0]+hole[0], table[1]+hole[1]))


x1 = 67.5
y1 = 127

# 목적구에서 구멍으로 가는 벡터의 각도(0~360)들 중 각이 가장 비슷한 값 찾기
target_hole_atan = list()
min_diff = (360, 0)


for hole in holes:
    dx = hole[1] - x1
    dy = hole[0] - y1
    target_atan_temp = math.atan2(dy, dx)
    target_hole_atan.append(target_atan_temp)

    print(target_hole_atan[-1])





