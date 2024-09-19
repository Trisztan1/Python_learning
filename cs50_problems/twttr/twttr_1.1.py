def main():
    user_input = input("Input: ").lower().strip()
    print(trim_vowels(user_input))

def trim_vowels(user_input):
    excluded_vowels = {"a", "e", "i", "o", "u"}
    output = [letter for letter in user_input if letter not in excluded_vowels]
    return "".join(output).capitalize()

main()