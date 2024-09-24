foods = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

prices = []

def main():
# get user input
    while True:
        try:
            user_input = input("Item: ").title().strip()

            if user_input not in foods:
                continue
            else:
                prices.append(foods[user_input])
    # print total
                print(f"Total: ${sum(prices):.2f}")

        except EOFError:
            break


main()