question = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").strip()

match question:
    case "42" | "Forty Two" | "forty-two":
        print("Yes")
    case _:
        print("No")