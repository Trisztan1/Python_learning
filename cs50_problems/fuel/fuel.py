def main():
    user_input = get_input("Fraction: ")
    percentage = convert_percentage(user_input)
    if percentage >= 99:
        print("F")
    elif percentage <= 1:
        print("E")
    else:
        print(f"{percentage}%")

def get_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            x, y = user_input.split("/")
            x = int(x)
            y = int(y)

            if x > y:
                continue

            return x / y
        except (ValueError, ZeroDivisionError):
            pass

def convert_percentage(user_input):
    return round(user_input * 100)



main()
