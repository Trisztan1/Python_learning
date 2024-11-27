def main():
    word = input("Input: ").strip()

    print(shorten(word))

def shorten(word):
    shortened_word = ""
    for letter in word:
        if letter not in ["A","E","I","O","U","a","e","i","o","u"]:
            shortened_word += letter
            

    return shortened_word



if __name__ == "__main__":
    main()