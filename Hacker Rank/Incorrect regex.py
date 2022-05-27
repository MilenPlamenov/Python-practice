import re

n = int(input())

for _ in range(n):
    pattern = input()

    try:
        re.compile(pattern)
        print("True")

    except re.error:
        print("False")
