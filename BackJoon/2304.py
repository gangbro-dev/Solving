N = int(input())

pillar = [0] * 1001
end_L = 0
for _ in range(N):
    L, H = map(int, input().split())
    pillar[L] = H
    end_L = max(end_L, L)

max_H = max(pillar)
max_L = pillar.index(max(pillar))

cnt = max_H

left_max_H = 0
for i in range(0, max_L):
    left_max_H = max(pillar[i], left_max_H)
    cnt += left_max_H

right_max_H = 0
for i in range(end_L, max_L, -1):
    right_max_H = max(pillar[i], right_max_H)
    cnt += right_max_H

print(cnt)
