import math
n = int(input())

for i in range(n):
    sheep = int(input())
    oagnili = sheep // 3
    oagnili *= 2
    the_half = sheep / 2
    all_sheep = oagnili + the_half - 1
    all_sheep /= 2
    print(math.ceil(sheep + all_sheep))
