
# def rstr(a):
#     # 1 b = a[-1::-1]
#
#     # 2 b = ''
#     #   for i in a:
#     #       b = i + b
#     #   return b
#
#     al = list(a)
#     b = True
#     for i in range(len(a)//2):
#         if al[i] != al[-1-i]:
#             b = False
#             break
#     return b
#
#
# print(rstr(a))

# def itoa(a):
#     result = ''
#     while a > 0:
#         i = a % 10
#         a = a // 10
#         result = chr(ord('0') + i) + result
#
#     return result
#
#
# a = 123456
# b = itoa(a)
# print(b)
# print(type(b))




