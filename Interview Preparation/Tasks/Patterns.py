def pattern_one(n):
    for i in range(n + 1):
        for j in range(i):
            print(i, end=' ')
        print()


# pattern_one(6)
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6

# ----------------------------------


def pattern_two(n):
    for i in range(0, n + 1):
        for j in range(i):
            print(j, end=' ')
        print()


# pattern_two(6)
# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4
# 0 1 2 3 4 5

# ------------------------------------


def pattern_three(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print(chr(65 + i), end=' ')
        print()


# pattern_three(6)
# A
# B B
# C C C
# D D D D
# E E E E E
# F F F F F F


# ---------------------------------------


def pattern_four(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print(chr(65 + j), end=' ')
        print()


# pattern_four(6)
# A
# A B
# A B C
# A B C D
# A B C D E
# A B C D E F


# --------------------------------------------


def pattern_five(n):
    num = 65
    for i in range(0, n):
        for j in range(0, i + 1):
            print(chr(num), end=' ')
            num += 1
        print()


# pattern_five(7)
# A
# B C
# D E F
# G H I J
# K L M N O
# P Q R S T U
# V W X Y Z [ \
