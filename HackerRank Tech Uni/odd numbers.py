from itertools import combinations


def the_whole_list_is_only_with_even_nums(numbers_list):
    for i in numbers_list:
        if i % 2 != 0:
            return False


def filter_the_list(numbers_list, max_s):
    for number in numbers_list:
        if number > max_s:
            numbers_list.remove(number)
    return numbers_list


def solve(numbers_list, max_s):
    counter = 0
    all_combinations = list(combinations(numbers_list, 2))
    for combination in all_combinations:
        combination_sum = sum(combination)
        if combination_sum % 2 != 0 and combination_sum <= max_s:
            counter += 1

    return counter


tests = int(input())

for _ in range(tests):
    list_len, max_sum = [int(i) for i in input().split()]
    nums_list = [int(i) for i in input().split()]
    if the_whole_list_is_only_with_even_nums(nums_list):
        print(0)
    else:
        filter_the_list(nums_list, max_sum)
        print(solve(nums_list, max_sum))

