rows, columns = map(int, input().split(" "))
matrix = []
matches = 0
for i in range(rows):
    row = input().split(" ")
    matrix.append(row)

for i in range(rows - 1):
    for j in range(columns - 1):
        current_char = matrix[i][j]

        if current_char == matrix[i][j + 1] and current_char == matrix[i + 1][j] and current_char == matrix[i + 1][
            j + 1]:
            matches += 1

print(matches)
