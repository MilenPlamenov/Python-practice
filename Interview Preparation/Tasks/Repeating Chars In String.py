str_input = input()

# from collections import Counter

# c = Counter(list(str_input))
# print(c.most_common(2))

dict_of_commons = {}

for element in str_input:
    if element not in dict_of_commons:
        dict_of_commons[element] = 1
    else:
        dict_of_commons[element] += 1

print({f"{k} - {v}" for k, v in dict_of_commons.items() if v == max(dict_of_commons.values())})

