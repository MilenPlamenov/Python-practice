def check_subset(set_one, set_two):
    if set_one.issubset(set_two):
        return "True"
    return "False"


n = int(input())

for _ in range(n):
    A_elements = int(input())  # in Python we dont need this tho
    A = set([int(i) for i in input().split()])

    B_elements = int(input())
    B = set([int(i) for i in input().split()])

    print(check_subset(A, B))


