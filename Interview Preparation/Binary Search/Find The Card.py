# find a card in sequence with least moves

# with linear search

cards = [18, 13, 10, 9, 8,  7, 5, 2, 1]
searched_card = 7


# def locate_card(cards, searched_card):
#     if cards:
#         for el in cards:
#             if el == searched_card:
#                 return cards.index(el)
#
#     return -1
#
#
# print(locate_card(cards, searched_card))

# with binary search


def locate_card_binary_search(cards, searched_card):
    low, high = 0, len(cards) - 1

    while low <= high:

        mid = (high + low) // 2

        if cards[mid] < searched_card:
            high = mid - 1

        elif cards[mid] > searched_card:
            low = mid + 1

        # means searched card is present at mid
        else:
            return mid

    return -1


print(locate_card_binary_search(cards, searched_card))