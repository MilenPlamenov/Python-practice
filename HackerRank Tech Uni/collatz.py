def check_collatz(number):
    if number == 1:
        return 1
    elif number == 2:
        return 2
    return 4


n = int(input())
for i in range(n):
    num = int(input())
    print(check_collatz(num))