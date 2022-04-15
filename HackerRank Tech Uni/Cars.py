n = int(input())

for _ in range(n):
    n_count = int(input())
    nums = [int(i) for i in input().split()]
    needed_n = max(nums)
    print(needed_n * 10)