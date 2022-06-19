from functools import reduce

ll = [5, 8, 10, 20, 50, 100]

s = reduce(lambda x, y: x+y, ll)
print(s)
