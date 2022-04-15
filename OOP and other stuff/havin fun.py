n = int(input())

the_order = []

for _ in range(n):
    part_of_the_order = int(input())
    the_order.append(part_of_the_order)

widgets_available = int(input())
orders = 0

for w in the_order:
    if widgets_available - w >= 0:
        orders += 1
    else:
        break

print(orders)