rows = int(input())

matrix = []
sum_primary_diagonal = []
sum_secondary_diagonal = []

for i in range(rows):
    row = list(map(int, input().split(", ")))
    matrix.append(row)

for i in range(rows):
    for j in range(rows):
        if i == j:
            sum_primary_diagonal.append(matrix[i][j])
        if (i + j) == (rows - 1):
            sum_secondary_diagonal.append(matrix[i][j])


print(f"Primary diagonal: {', '.join([str(i) for i in sum_primary_diagonal])}. Sum: {sum(sum_primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(i) for i in sum_secondary_diagonal])}. Sum: {sum(sum_secondary_diagonal)}")



