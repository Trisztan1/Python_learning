import sys

def main():
    check_command_line_arg()

    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    
    except FileNotFoundError:
        sys.exit("File does not exist")
    
    count_lines = 0
    for line in lines:
        if check_line(line):
            continue
        else:
            count_lines += 1
    
    print(count_lines)


def check_command_line_arg():
    extensions = [".py"]
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line argument")

    found = any(sys.argv[1].endswith(ext) for ext in extensions)

    if not found:
        sys.exit("Not a Python file")

def check_line(line):
    if line.isspace():
        return True
    
    if line.lstrip().startswith("#"):
        return True
    
    return False

if __name__ == "__main__":
    main()