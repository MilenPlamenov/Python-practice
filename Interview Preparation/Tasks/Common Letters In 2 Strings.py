string_one = input()
string_two = input()

ll = list(set(string_one) & set(string_two))

print([i for i in ll])

