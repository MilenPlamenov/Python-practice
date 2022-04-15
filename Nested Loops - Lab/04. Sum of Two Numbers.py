start = int(input())
end = int(input())
counter = 0
magic_num = int(input())
is_found = False

for num1 in range(start, end + 1):
    for num2 in range(start, end + 1):
        counter += 1
        if num1 + num2 == magic_num:
            print(f"Combination N:{counter} ({num1} + {num2} = {magic_num})")
            is_found = True
            break
    if is_found:
        break

if not is_found:
    print(f"{counter} combinations - neither equals {magic_num}")