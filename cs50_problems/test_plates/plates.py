import string

def main():
    plate = input("Plate: ").strip()
    print(is_valid(plate))

def is_valid(plate):
    if len(plate) < 2 or len(plate) > 6 or plate[:2].isdigit():
        return "Invalid"
    
    if any(char for char in plate if char in string.punctuation or char.isspace()):
        return "Invalid"

    for i, char in enumerate(plate):
        if char.isdigit():
            if char == "0":
                return "Invalid"
            if not plate[i:].isdigit():
                return "Invalid"
            break
    
    return "Valid"
        
    


if __name__ == "__main__":
    main()
