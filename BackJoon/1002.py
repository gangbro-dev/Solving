def distance(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    return round((dx**2 +dy**2)**(1/2), 5)

T = int(input())
InKeys = ['x1', 'y1', 'r1', 'x2', 'y2', 'r2']
Indict = []
for test_cnt in range(T):
    InValues = (list(map(int, input().split())))
    Indict= dict(zip(InKeys, InValues))
    turret_distance = distance(
        Indict['x1'],
        Indict['y1'],
        Indict['x2'],
        Indict['y2'],
    )
    if turret_distance == 0:
        if Indict['r1'] == Indict['r2']:
            point = -1
        else:
            point = 0
    elif turret_distance < abs(Indict['r1'] - Indict['r2']):
        point = 0
    elif turret_distance == abs(Indict['r1'] - Indict['r2']):
        point = 1
    elif turret_distance < Indict['r1'] + Indict['r2']:
        point = 2
    elif turret_distance == Indict['r1'] + Indict['r2']:
        point = 1
    elif turret_distance > Indict['r1'] + Indict['r2']:
        point = 0
    
    print(point)
