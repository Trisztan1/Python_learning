def main():
    camelCase = input("camelCase: ")
    print(convert_snake(camelCase))

def convert_snake(camelCase):
    snake_case = []
    for letter in camelCase:
        if letter.isupper():
            snake_case.append(f"_{letter.lower()}")
        else:
            snake_case.append(letter)
            
    return "".join(snake_case)


main()