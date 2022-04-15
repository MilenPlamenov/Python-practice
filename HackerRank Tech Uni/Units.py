n = int(input())


for _ in range(n):
    number = int(input())
    for k in range(number - 1, 0, -1):
        number = str(k) + str(number) + str(k)
    print(number)
