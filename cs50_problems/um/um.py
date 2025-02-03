import re
import sys

def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\b([uU][mM])\b"
    matches = re.findall(pattern, s)
    counter = 0
    
    for _ in matches:
        counter += 1
    
    return counter


if __name__ == "__main__":
    main()