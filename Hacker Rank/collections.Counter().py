num_of_shoes = int(input())

shoe_sizes = [int(i) for i in input().split()]

n = int(input())
total = 0
for i in range(n):
    arr = input().split()
    size = int(arr[0])
    price = int(arr[1])

    if size in shoe_sizes:
        shoe_sizes.remove(size)
        total += price

print(total)