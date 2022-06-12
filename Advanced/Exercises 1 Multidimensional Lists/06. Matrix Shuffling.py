rows, columns = map(int, input().split(" "))
matrix = []

for i in range(rows):
    row = list(input().split(" "))
    matrix.append(row)

command = input()
size = len(matrix)
while command != "END":
    command = command.split()
    if command[0] == "swap" and len(command) == 5:
        first_row = int(command[1])
        first_col = int(command[2])
        second_row = int(command[3])
        second_col = int(command[4])
        if 0 <= first_row < rows and 0 <= first_col < columns and 0 <= second_row < rows and 0 <= second_col < columns:
            matrix[first_row][first_col], matrix[second_row][second_col] = matrix[second_row][second_col], \
                                                                           matrix[first_row][first_col]
            for line in matrix:
                print(' '.join(map(str, line)))
        else:
            print("Invalid input!")
            command = input()
            continue
    else:
        print("Invalid input!")
    command = input()
