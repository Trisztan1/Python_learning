import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(html):
    if re.search(r"<iframe(.)*><\/iframe>", html):
        pattern = (
            r"src=\"https?:\/\/(www\.)?youtube\.com\/embed\/(?P<catch_this>[\w\d-]+)\""
        )

        match = re.search(pattern, html)
        if match:
            return f"https://youtu.be/{match.group("catch_this")}"


if __name__ == "__main__":
    main()
