from itertools import combinations_with_replacement

string_input, replacements = input().split()

all_combinations = list(combinations_with_replacement(string_input, int(replacements)))
for combination in all_combinations:
    print("".join(combination))
