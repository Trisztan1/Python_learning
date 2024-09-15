while True:
    message = input("Write something here: ")
    modified_message = message.replace(" ", "...")
    print(modified_message)
    option = input("Would you like to quit? y/n ").lower()
    if option == "y":
        break