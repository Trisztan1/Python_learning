import random
from pyfiglet import Figlet
import sys

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid input")
    if sys.argv[2] not in fonts:
        sys.exit("Error non existed font")

    user_input = input("Input: ").strip()
    
    if len(sys.argv) == 1:
        font_type = random.choice(fonts)
        figlet.setFont(font=font_type)
        text = figlet.renderText(user_input)
        print(text)
    elif len(sys.argv) == 3:
        figlet.setFont(font=sys.argv[2])
        text = figlet.renderText(user_input)
        print(text)
    


main()