from itertools import product

n = int(input())
com = []
for _ in range(n):
    num = int(input())
    chars_for_the_combination = ""
    for i in range(num):
        chars_for_the_combination += chr(65 + i)

    all_combinations = sorted(list(product(chars_for_the_combination, repeat=3)))
    max_index = num + 1
    index = 1
    for combination in all_combinations:
        if index == max_index:
            break
        if combination not in com:
            com.append(combination)
            index += 1

for comb in sorted(com):
    print(''.join(comb))
