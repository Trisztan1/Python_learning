def main():
    user_input = input("Input: ").strip()
    print(trim_vowels(user_input))

def trim_vowels(user_input):
    excluded_vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    output = [letter for letter in user_input if letter not in excluded_vowels]
    return "".join(output)

main()