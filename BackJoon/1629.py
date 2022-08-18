# A 제곱의 나머지 = ((A%C) * A)%C => 시간초과 실패
# if A**B < C:
#     ans = A**B
# else:
#     rest = []
#     i = 1 % C
#     while i not in rest:
#         rest.append(i)
#         i = (rest[-1] * A) % C
#
#     loop_start = rest.index(i)
#     loop = len(rest) - loop_start
#
#     ans = rest[((B-loop_start) % loop)+loop_start]
# print(ans)
print(pow(*map(int, input().split())))
# 시발 내장함수
