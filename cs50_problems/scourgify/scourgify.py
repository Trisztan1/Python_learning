import sys
import csv

def main():
    check_arguments(sys.argv)
    try:
        write_new_file(sys.argv[1], sys.argv[2])

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")



def check_arguments(args):
    if len(args) > 3:
        sys.exit("Too many comand-line arguments")
    elif len(args) < 3:
        sys.exit("Too few command-line arguments")


def write_new_file(o_file, n_file):
    names = []
    new_names = []

    # Append and read the file

    with open(o_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            names.append({"name": row["name"], "house": row["house"]})


    # Treat the names variable separate first names and last names

    for name in names:
        house = name["house"]
        last, first = name["name"].split(", ")
        new_names.append({"first": first.strip(), "last": last.strip(), "house": house.strip()})

    with open(n_file, "w", newline="") as new_file:
        writer = csv.DictWriter(new_file, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for row in new_names:
            writer.writerow(row)


if __name__ == "__main__":
    main()
