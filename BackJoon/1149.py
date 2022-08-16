N = int(input())

cost = 0
RGB = []
result = 1000*1000
for RGB_idx in range(N):
    temp_idx = [RGB_idx]
    RGB.append(temp_idx + list(map(int, input().split())))



print(result)

