from itertools import combinations

total_chars = int(input())

replacements = int(input())

chars_for_the_combination = ""

for i in range(total_chars):
    chars_for_the_combination += chr(65 + i)

all_combinations = list(combinations(chars_for_the_combination, replacements))

for combination in all_combinations:
    print("".join(combination))

# I love this one <3
