def main():
    camelCase = input("camelCase: ")
    convert_snake(camelCase)

def convert_snake(camelCase):
    for letter in camelCase:
        if letter.isupper():
            letter = letter.replace(letter, f"_{letter.lower()}")
        print(letter, end="")
        
main()