import random


def play_game(searched_n, input_n, attempt):
    while True:
        if searched_n == input_n:
            print(f"You won the game! Number of attempts: {attempt}")
            break
        else:
            if input_n > searched_n:
                print("lower")
            else:
                print("higher")
            attempt += 1
            input_n = int(input("Type number from 0 to 100: "))


searched_num = random.randint(0, 100)
input_num = int(input("Type number from 0 to 100: "))
attempts = 0


play_game(searched_num, input_num, attempts)


