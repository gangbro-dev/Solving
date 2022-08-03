# 방법 1. 추 집합의 모든 부분집합을 구해서 그 집합의 원소합을 구한다.
# 원소합으로 이루어진 set을 사용하면, 빈 구멍을 바로 찾울 수 있다.
# -> 실패 메모리 오버
# 함수 지역변수를 이용해서 메모리 사용을 줄여보자!
# -> 실패 메모리 오버
# 방법 2. 1부터 숫자를 하나씩 올리면서 추 무게조합으로 구현가능한지 체크한다.
# 어케함?
# 문제1. 그 숫자를 만들기 위한 추의 종류를 특정할 수 없다.
# 문제2. 추를 중복으로 사용하지 않으려면 사용한 추들을 표시해야 한다.
# 딕셔너리 키 값을 확인할 수로 하고, 밸류로 쓴 원소를 표기한다?
# 입력값 받기
N = int(input())
weight = list(map(int, input().split()))
weight.sort()

check_dict = {}
for i in range(N):
    check_dict[weight[i]] = weight[i:i+1]

cnt = 1
while True:
    #이번 루프 이전에 key값들 저장
    keys = check_dict.keys()
    if not cnt in keys:
        temp_dict = {}
        for i in keys:
            if i < cnt:
                weight_temp = weight[:]
                for j in check_dict[i]:
                    weight_temp.remove(j)
                for j in weight_temp:
                    if not i+j in keys:
                        temp_dict[i+j] = check_dict[i].append(j)
    
    check_dict.update(temp_dict)
    
    if not cnt in keys:
        break
    cnt += 1

print(cnt)
