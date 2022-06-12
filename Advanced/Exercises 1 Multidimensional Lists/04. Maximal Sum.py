from sys import maxsize


def take_current_sum(matrix, row, col):
    return matrix[row][col] + matrix[row + 1][col] + matrix[row + 2][col] + matrix[row][col + 1] + matrix[row][
        col + 2] + matrix[row + 1][col + 1] + matrix[row + 2][col + 1] + matrix[row + 1][col + 2] + matrix[row + 2][
               col + 2]


rows, columns = map(int, input().split(" "))
matrix = []
max_sum = -maxsize
position = ()
for i in range(rows):
    row = list(map(int, input().split(" ")))
    matrix.append(row)

for row in range(rows - 2):
    for col in range(columns - 2):
        curr_sum = take_current_sum(matrix, row, col)
        if curr_sum > max_sum:
            position = (row, col)
            max_sum = curr_sum

row, col = position
print(f"Sum = {max_sum}")
print(matrix[row][col], matrix[row][col + 1], matrix[row][col + 2])
print(matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2])
print(matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2])
