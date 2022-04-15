#cols always 2

all_rectangles = []

n = int(input())
cols = int(input())

for i in range(n):
    sides = [int(j) for j in input().split()]
    all_rectangles.append(sides)

new_amounts = []
for rect in all_rectangles:
    new_amounts.append(rect[0]/rect[1])

check = True
element_zero = new_amounts[0]
for item in new_amounts:
    if item != element_zero:
        check = False
        break

if check:
    print(len(new_amounts))

total_equal_values = 0
for i in range(len(new_amounts)):
    try:
        if new_amounts[i] == new_amounts[i + 1]:
            total_equal_values += 1
    except IndexError:
        break

print(total_equal_values)



