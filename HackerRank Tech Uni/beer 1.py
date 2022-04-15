from itertools import combinations
input_string = input()

while input_string != "0 0":
    try:
        n, money = [int(i) for i in input_string.split()]
        prices_per_beer = ""
        total_beers = 0
        for _ in range(n):
            curr_num = input()
            prices_per_beer += curr_num

        all_combinations = list(combinations(prices_per_beer, 2))
        for combination in all_combinations:
            if sum([int(i) for i in combination]) <= money:
                total_beers += 1
        print(total_beers)
        input_string = input()
    except EOFError:
        break



