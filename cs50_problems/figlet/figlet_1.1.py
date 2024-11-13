import random
from pyfiglet import Figlet
import sys

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        font_type = random.choice(fonts)
        figlet.setFont(font=font_type)

    elif len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("s")
        if sys.argv[2] not in fonts:
            sys.exit("s")

        figlet.setFont(font=sys.argv[2])

    else:
        sys.exit("s")

    user_input = input("Input: ").strip()
    text = figlet.renderText(user_input)
    print(text)


main()
