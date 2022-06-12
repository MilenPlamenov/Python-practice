rows, cols = [int(i) for i in input().split(", ")]
matrix_sum = 0
matrix = []

for i in range(rows):
    row = list(map(int, input().split(", ")))
    matrix.append(row)


for i in range(rows):
    for j in range(cols):
        matrix_sum += matrix[i][j]

print(matrix_sum)

print(matrix)