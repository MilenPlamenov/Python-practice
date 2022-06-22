def get_missing_number(list_input):
    return list(set(range(list_input[len(list_input) - 1])[1:]) - set(list_input))[0]
    # take the full set and subtract the actual one then parse it to list and take the 1st el


ll = list(range(1, 100))
ll.remove(40)
print(get_missing_number(ll))
