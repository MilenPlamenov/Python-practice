import roman

for i in range(3):
    roman_num_input = input()
    if len(roman_num_input) == 2:
        if roman.fromRoman(roman_num_input[::-1]) < roman.fromRoman(roman_num_input):
            roman_num_input = roman_num_input[::-1]

    print(roman_num_input)





