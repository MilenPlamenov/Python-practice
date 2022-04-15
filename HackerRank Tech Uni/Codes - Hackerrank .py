n = int(input())
smallest_code = 999999999
smallest_word = ""

for _ in range(n):
    word = input()
    number = 0
    for letter in word:
        number += ord(letter) - 96

    if number < smallest_code:
        smallest_code = number
        smallest_word = word

print(smallest_word, smallest_code)