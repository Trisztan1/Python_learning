def main():
    name = input("What's your name? ").strip().capitalize()
    if name == "":
        hello()
    else:
        hello(name)


# This is a comment


def hello(to="world"):
    print(f"Hello, {to}")


main()
