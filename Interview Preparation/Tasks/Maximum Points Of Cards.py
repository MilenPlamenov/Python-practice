def all_suits_are_the_same(cards_list):
    first_card_suit = cards_list[0][0]
    for i in range(1, len(cards_list)):
        if cards_list[i][0] != first_card_suit:
            return False
    return True


def all_numbers_are_same(cards_list):
    first_card_number = cards_list[0][1]
    for i in range(1, len(cards_list)):
        if cards_list[i][1] != first_card_number:
            return False
    return True


def all_numbers_are_aces(cards_list):
    for el in cards_list:
        if el[1] != 'A':
            return False
    return True


t = int(input())  # tests

for _ in range(t):
    n = int(input())  # num of cards for each test in python this is useless cause its high level language !!
    cards = input().split()
    total_sum_per_test = 0
    if all_numbers_are_same(cards) and all_numbers_are_aces(cards):
        print(200)
        continue
    elif all_numbers_are_same(cards) and not all_numbers_are_aces(cards):
        print(100)
        continue
    if all_suits_are_the_same(cards):
        for card in cards:
            if card[1] in ['J', 'Q', 'K']:
                total_sum_per_test += 10
            elif card[1] == 'A':
                total_sum_per_test += 11
            else:
                total_sum_per_test += int(card[1])
        print(total_sum_per_test)
    else:
        if any([x[1] == 'A' for x in cards]):
            print(11)
            continue
        elif any([x[1] in ['J', 'Q', 'K'] for x in cards]):
            print(10)
            continue
        else:
            print(max([int(x[1]) for x in cards]))

