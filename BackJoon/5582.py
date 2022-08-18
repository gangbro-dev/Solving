def lcs(a, b):
    astr = ' ' + a
    bstr = ' ' + b
    max_value = 0
    mat = [[0]*(len(astr)) for _ in range(len(bstr))]
    for row in range(len(bstr)):
        for column in range(len(astr)):
            if row == 0 or column == 0:
                mat[row][column] = 0
            elif astr[column] == bstr[row]:
                mat[row][column] = mat[row-1][column-1] + 1
                max_value = max(mat[row][column], max_value)
            else:
                mat[row][column] = 0
    return max_value


A = input()
B = input()
print(lcs(A, B))
