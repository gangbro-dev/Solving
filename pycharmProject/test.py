from itertools import combinations

A = [1, 1, 2, 3, 3, 4, 4, 4]
for i in combinations(A, 4):
    print(i)
