tests = int(input())

t9_dict = {
    1: ' ',
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'Q', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'W', 'Z'],
}

list_of_words = []
current_buttons_before_space = []
for _ in range(tests):
    number_of_words_in_the_dict = int(input())
    for _ in range(number_of_words_in_the_dict):
        current_word = input()
        list_of_words.append(current_word)

    keyboard_clicks = int(input())
    clicked_buttons = [int(i) for i in input().split()]
    generated_string = ''
    for button in clicked_buttons:
        if button != 1:
            current_buttons_before_space.append(button)
        else:
            # 2 6 2 4
            for btn in current_buttons_before_space:
                pass

            current_buttons_before_space = []
