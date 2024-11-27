def main():
    word = input("Input: ").strip()
    print(shorten(word))

def shorten(word):
    vowels = ["A","E","I","O","U","a","e","i","o","u"]

    return "".join(letter for letter in word if letter not in vowels)


if __name__ == "__main__":
    main()