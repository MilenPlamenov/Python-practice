def countSetBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


n = int(input())

for _ in range(n):
    total = 0
    nums = [int(i) for i in input().split()]
    for num in nums:
        total += countSetBits(num)
    print(total)


