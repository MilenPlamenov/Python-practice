from itertools import permutations


def possible_permutations(seq):
    all_permutations = list(permutations(seq))
    for p in all_permutations:
        yield list(p)


[print(n) for n in possible_permutations([1, 2, 3])]