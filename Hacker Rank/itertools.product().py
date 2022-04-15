from itertools import product

l_one = [int(i) for i in input().split()]
l_two = [int(i) for i in input().split()]

print(*list(product(l_one, l_two)))