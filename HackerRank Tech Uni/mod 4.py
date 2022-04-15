input_string = input()

while input_string != "0":
    try:
        n = int(input_string)
        for _ in range(n):
            current_nums = input().split()
            number = int(current_nums[0])
            power = int(current_nums[1])
            mod = int(current_nums[2])
            print(pow(number, power, mod))
        input_string = input()
    except EOFError:
        break