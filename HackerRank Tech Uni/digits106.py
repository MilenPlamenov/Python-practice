n = int(input())

for _ in range(n):
    nums = input()
    total = 0
    num_multiplier = len(nums) - 1

    for num in nums:
        total += int(num) * num_multiplier

    print(total)