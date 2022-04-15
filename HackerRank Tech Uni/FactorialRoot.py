n = int(input())


for i in range(n):
    number = int(input())
    if number >= 6:
        print(9)
    else:
        factorial_number = 1
        sum_of_the_chars = 0
        for fact in range(number, 0, -1):
            factorial_number *= fact

        for f in str(factorial_number):
            sum_of_the_chars += int(f)

        print(sum_of_the_chars)

# working !


