import math
n = int(input())


def leastcommonmultiple(num_one, num_two, lcm):
    for i in range(num_two, num_two * 2):
        if i % num_one == 0 and i % num_two == 0:
            return i
    return num_one * num_two


for _ in range(n):
    num = int(input())
    for i in range(num + 1, num * 2):
        lcm = i
        leastcommonmultiple(num, i, lcm)
        result = lcm / num - i / i

        if lcm % result == 0:
            print(f"{i} {lcm / result}")










