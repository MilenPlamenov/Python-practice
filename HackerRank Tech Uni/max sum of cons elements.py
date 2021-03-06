from sys import maxsize


def max_sub_array_sum(a):
    max_so_far = -maxsize - 1
    max_ending_here = 0

    for i in range(0, len(a)):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))

print(max_sub_array_sum(arr))