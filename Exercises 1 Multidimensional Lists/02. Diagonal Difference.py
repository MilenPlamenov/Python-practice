rows = int(input())
matrix = []

for i in range(rows):
    row = list(map(int, input().split(" ")))
    matrix.append(row)
sum_primary = 0
sum_secondary = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:                          # primary diagonal
            sum_primary += matrix[i][j]
        if (i + j) == (rows - 1):           # secondary diagonal
            sum_secondary += matrix[i][j] 

print(abs(sum_primary - sum_secondary))