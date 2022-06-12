string_one = input()
string_two = input()

a = list(set(string_one) & set(string_two))

print([i for i in a])

