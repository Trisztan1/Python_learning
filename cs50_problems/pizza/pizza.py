import sys
from tabulate import tabulate
import csv


def main():
    check_argv(sys.argv)
    print_ASCII_menu(sys.argv[1])


def check_argv(args):
    extensions = [".csv"]
    if len(args) > 2:
        sys.exit("Too many command-line arguments")
    elif len(args) < 2:
        sys.exit("Too few command-line arguments")

    found = any(args[1].endswith(ext) for ext in extensions)
    if not found:
        sys.exit("Not a CSV file")

    # found = True

    # for ext in extensions:
    #     if not args[1].endswith(ext):
    #         found = False

    # if not found:
    #     sys.exit("Not a CSV file")


def print_ASCII_menu(arg):
    menu = []
    with open(arg, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            menu.append(row)

    print(tabulate(menu, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
