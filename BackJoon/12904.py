# S = input()
# T = input()
# 실패인듯
# BinS = S.count('B')
# BinT = T.count('B')
# # B 개수가 적다면 애초에 불가능
# if BinT < BinS:
#     print(0)
# # B개수가 같다면 뒤에 A붙이기만 가능함
# elif BinT == BinS:
#     if T.lstrip(S).rstrip('A'):
#         print(0)
#     else:
#         print(1)
# # 아니라면 좀 복잡하다
# else:
#     # 뒤집기는 연산이 많이 필요하므로 안뒤집고 결과를 만들어 보자
#     # S에 앞 뒤로 붙이기 연산만 해서 뒤집기를 없앤다.
#     # B 개수를 비교해서 마지막 결과가 뒤집힌 채 인지 아닌지 판별
#     if (BinT - BinS) % 2:
#         T = T[::-1]
#     # print(T)
#     # S 가 가능한 위치 찾기
#     # S는 B를 붙이면 뒤집히므로, T 내부에서 S를 기준으로 무조건 앞뒤 B 개수가 같거나, 앞이 한개 많은 위치에서 시작해야함.
#     BP = ((BinT - BinS) // 2) + ((BinT - BinS) % 2)
#     idx = T.find('B')
#     cnt = 1
#     while cnt <= BP:
#         idx = T.find('B', idx+1)
#         cnt += 1
#     # 구한 위치를 이용해서 StartIdx, EndIdx 찾기
#     start = S.find('B')
#     if start == -1:
#         start = idx + 1
#     else:
#         start = idx - start
#     end = start + len(S)
#     # 이 위치에 S가 존재하는지 확인 존재한다면 조건에 맞게 인덱스 옮기기
#     if T[start: end] == S:
#         # 초기값
#         rev = False
#         ans = 1
#         while end - start < len(T):
#             if rev:
#                 if 0 <= start:
#                     if T[start - 1] == 'A':
#                         start -= 1
#                     elif T[end] == 'B':
#                         end += 1
#                         rev = False
#                     else:
#                         ans = 0
#                         break
#                 elif end < len(T):
#                     if T[end] == 'B':
#                         end += 1
#                         rev = False
#                     else:
#                         ans = 0
#                         break
#             else:
#                 if end < len(T):
#                     if T[end] == 'A':
#                         end += 1
#                     elif T[start] == 'B':
#                         start -= 1
#                         rev = True
#                     else:
#                         ans = 0
#                         break
#                 elif 0 <= start:
#                     if T[start] == 'B':
#                         start -= 1
#                         rev = True
#                     else:
#                         ans = 0
#                         break
#             # print(T[start:end])  #################
#         print(ans)
#     else:
#         print(0)

## 2번 아이디어

# T에서 S로 가자
S = input()
T = input()
A = 'A'
B = 'B'
rev = False
start = 0
end = len(T)
while end - start > len(S):
    if not rev:
        if T[end - 1] == B:
            rev = True
        end -= 1
    else:
        if T[start] == B:
            rev = False
        start += 1
    # if not rev:
    #     print(T[start:end])
    # else:
    #     if start:
    #         print(T[end - 1:start - 1:-1])
    #     else:
    #         print(T[end - 1::-1])
if not rev:
    print(int(T[start:end] == S))
else:
    if start:
        print(int(T[end - 1:start - 1:-1] == S))
    else:
        print(int(T[end - 1::-1] == S))
