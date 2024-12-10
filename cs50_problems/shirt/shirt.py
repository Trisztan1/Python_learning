import sys
from PIL import Image, ImageOps


def main():
    argument_check(sys.argv)
    try:
        image_processor(sys.argv)
    except FileNotFoundError:
        sys.exit("File not found")


def argument_check(args):
    extensions = [".png", ".jpg", ".jpeg"]
    match_extension = ""
    argument_parts = args[1].split(".")
    match_extension = argument_parts[-1]

    if len(args) > 3:
        sys.exit("Too many command-line arguments")
    elif len(args) < 3:
        sys.exit("Too few command-line arguments")

    for arg in args[1:]:
        if not any(arg.endswith(ext) for ext in extensions):
            sys.exit("Invalid input")

    # Here os.path.splitext() would be better

    if not args[2].endswith(match_extension):
        sys.exit("Input and output have different extensions")


def image_processor(args):
    size = (600, 600)
    with Image.open(args[1]) as im, Image.open("shirt.png") as shirt:
        output_image = ImageOps.fit(im, size)
        output_image.paste(shirt, (0, 0), mask=shirt)
        output_image.save(args[2])


if __name__ == "__main__":
    main()
