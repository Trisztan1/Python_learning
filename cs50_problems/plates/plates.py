def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    invalid_first = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    invalid_input = [" ", ",", "."]
    if len(s) < 2 or len(s) > 6 or s[-2] == "0":
        return False
    
    for char in s:
        if char in invalid_input:
            return False
    
    for char in s[:-2]:
        if char in invalid_first:
            return False

    return True
main()