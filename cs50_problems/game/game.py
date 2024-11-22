import random

def main():
    level = get_level()
    number = random.randint(1, level)

    while True:
        guess = get_guess()

        if guess < number:
            print("Too small!")
        elif guess > number or guess > level:
            print("Too large!")
        else:
            print("Just right!")
            break


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass

def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
        except ValueError:
            pass


main()
