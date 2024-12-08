import sys


def main():
    is_argv_correct(sys.argv)

    row_count = 0

    try:
        with open(f"{sys.argv[1]}", "r") as file:
            for row in file:
                # if row == "\n" or row.startswith("#"):
                #     continue
                if row.strip() == "" or row.strip().startswith(
                    "#"
                ):  # This works better then the previous one
                    continue

                row_count += 1

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(row_count)


def is_argv_correct(input):
    extensions = [".py"]

    if len(input) > 2:
        sys.exit("Too many command-line arguments")
    elif len(input) < 2:
        sys.exit("Too few command-line argument")

    found = any(input[1].endswith(ext) for ext in extensions)

    if not found:
        sys.exit("Not a Python file")

    # This is the SAME as above

    # found = False
    # for ext in extensions:
    #     if input[1].endswith(ext):
    #         found = True
    #         break

    # if not found:
    #     sys.exit("Not a Python file")


main()
