# Write a program to find the sum of the digits of a number in Python?

n = int(input())
total = 0
for el in str(n):
    total += int(el)

print(total)
