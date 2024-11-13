import emoji
def main():
    user_input = input("Input: ")
    emoticon = emoji.emojize(user_input, language = "alias")
    print(emoticon)

if __name__ == "__main__":
    main()
