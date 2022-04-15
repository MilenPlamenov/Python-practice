tests = int(input())

for i in range(tests):
    n = int(input())
    boys_per_test = 0
    for j in range(n):
        current_egn = input()
        if int(current_egn[8]) % 2 == 0:
            boys_per_test += 1
    print(boys_per_test)


