from itertools import permutations

input_string = input().split()
the_r = int(input_string.pop())
input_string = "".join(input_string)

p = permutations(input_string, the_r)

for i in sorted(list(p)):
    print("".join(i))

# print(sorted(permutations("".join(input_string), the_r)))
