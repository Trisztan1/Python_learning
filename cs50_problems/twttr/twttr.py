def main():
    user_input = input("Input: ").strip()
    print(trimm_vowels(user_input))



def trimm_vowels(user_input):
    excluded_vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    output = []
    for letter in user_input:
        if letter in excluded_vowels:
            continue
        else:
            output.append(letter)
    return "".join(output)

main()
