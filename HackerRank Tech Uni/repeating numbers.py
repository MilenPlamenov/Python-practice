# from collections import Counter

# n = int(input())


# for i in range(n):
#     array_num = int(input())
#     array = sorted([int(i) for i in input().split()])
#     counter = Counter(array)
#     most_common = counter.most_common()
#     print(most_common[0][0])

# ------------
# nums = {}
#
# n = int(input())
# for i in range(n):
#     array_num = int(input())
#     array = sorted([int(i) for i in input().split(" ")])
#     for num in array:
#         if num not in nums:
#             nums[num] = 1
#         else:
#             nums[num] += 1
#
#     for k, v in sorted(nums.items(), key=lambda item: item[1], reverse=True):
#         print(k)
#         break
#
#     nums.clear()


# ---------------


# for i in range(n):
#     array_n = int(input())
#     arr = [int(i) for i in input().split()]
#     print(max(set(arr), key=arr.count))

# -----------------

def most_frequent(list_of_nums):
    counter = 0
    num = list_of_nums[0]

    for i in sorted(list_of_nums):
        curr_frequency = list_of_nums.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i

    return num


n = int(input())
for _ in range(n):
    nums = int(input())
    array = [int(i) for i in input().split()]
    print(most_frequent(array))

# -------------
# 5
# 5
# 100 100 200 300 300
# 6
# 5 4 3 2 1 6
# 10
# 10000 1000 10 1000 1000 1000 100 1 1 1
# 8
# 1 1 5 3 3 4 4 4
# 18
# 11 22 33 33 44 55 44 33 44 33 33 44 55 66 44 77 88 99
