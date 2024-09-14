import random
def get_guess():
    guess = int(input("Enter a guess: "))
    return guess

guess_count = 0
guess_limit = 4
x = random.randint(1,10)

while guess_count < guess_limit:
    guess = get_guess()
    guess_count = guess_count + 1
    if x == guess:
        print(f"You won! {get_guess()} is the number!")
        option = input("Play again. Y/N ")
        if option != "y":
            print("Thanks for playing!")
            break
        else:
            guess_count = 0
            x = random.randint(1,10)
    else:
        print("Sorry, wrong guess!")
    
    if guess_count == guess_limit:
        option = input("Try again. Y/N ").lower()
        if option != "y":
            print("Thanks for playing!")
            break
        else:
            guess_count = 0
            x = random.randint(1,10)